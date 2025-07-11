import logging
import typing
import uuid

from datetime import datetime, timezone
from enum import StrEnum

from PySide6.QtCore import (
    QAbstractTableModel,
    QModelIndex,
    QObject,
    Qt,
    Signal,
    Slot,
    QDateTime,
)
from PySide6.QtWidgets import QDialog, QMessageBox, QInputDialog

from ..models import (
    SubjectTask,
    EditedSubjectTask,
    EditedTaskWithID,
    SortByComboBoxEnum,
    SortAndFilterState,
)
from ..ui.add_task_dialog import Ui_AddTaskDialog

if typing.TYPE_CHECKING:
    from ..main import MainWindow


logger: logging.Logger = logging.getLogger("task-todos")


class EmitDialogInfoAs(StrEnum):
    add = "add"
    edit = "edit"


class TaskTodosTableModel(QAbstractTableModel):
    def __init__(self, /, parent: "TaskTodosController" = None):
        super().__init__(parent)
        self.todo_ctrl = parent

        self._display_data: list[list[str | datetime]] = []
        self._item_data: list[SubjectTask] = []

        self._col_headers: list[str] = ["Completed", "Subject", "Task", "Deadline"]

    def rowCount(self, /, parent=QModelIndex()):
        return len(self._item_data)

    def columnCount(self, /, parent=QModelIndex()):
        return len(self._col_headers)

    def data(self, index, /, role):
        if role == Qt.ItemDataRole.UserRole:
            return self._item_data[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            value = self._display_data[index.row()][index.column()]
            if isinstance(value, datetime):
                local_value = value.astimezone()
                return local_value.strftime("%x %X")

            if isinstance(value, bool):
                if value:
                    return "Yes"
                else:
                    return "No"

            if value is None:
                logger.debug(
                    "Received 'None' value at cell [%d, %d]",
                    index.row(),
                    index.column(),
                )
                return ""

            return value

        return None

    def headerData(self, section, orientation, /, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return self._col_headers[section]

        if orientation == Qt.Orientation.Vertical:
            return super().headerData(section, orientation, role)

    def load_tasks(self, tasks: list[SubjectTask]):
        self.beginResetModel()

        self._display_data.clear()
        self._item_data.clear()

        logger.debug("Cleared all tasks")

        for task in tasks:
            display_data = [task.completed, task.subject, task.task, task.deadline]
            self._display_data.append(display_data)

            self._item_data.append(task)

        logger.debug("Added %d tasks to model", len(self._item_data))
        self.endResetModel()

    def add_task(self, task: SubjectTask):
        display_data = [task.completed, task.subject, task.task, task.deadline]

        self._item_data.append(task)
        self._display_data.append(display_data)

        self.layoutChanged.emit()

    def delete_task(self, index: QModelIndex):
        del self._item_data[index.row()]
        del self._display_data[index.row()]

        self.layoutChanged.emit()

    def update_task(self, index: QModelIndex, task: SubjectTask):
        if not index.isValid():
            return

        display_data = [task.completed, task.subject, task.task, task.deadline]
        row = index.row()

        self._item_data[row] = task
        self._display_data[row] = display_data

        top = self.index(row, 0)
        bottom = self.index(row, self.columnCount() - 1)

        self.dataChanged.emit(top, bottom)


class TaskTodosController(QObject):
    def __init__(self, mw_parent: "MainWindow"):
        super().__init__(mw_parent)
        self.mw_parent = mw_parent

        self.ui = mw_parent.ui
        self.app_data = mw_parent.app_data

        self.subject_ctrl: SubjectItemController = SubjectItemController(self)
        self.task_ctrl: TasksItemController = TasksItemController(self)

        self.sort_filter_ctrl: SortAndFilterController = SortAndFilterController(self)
        self.setup()

    def setup(self):
        self.ui.filterBySubjectComboBox.addItems(self.app_data.subjects)

        self.subject_ctrl.subjectAdded.connect(self.subject_added)
        self.subject_ctrl.subjectRemoved.connect(
            self.ui.filterBySubjectComboBox.removeItem
        )

        self.ui.actionAdd_subject.triggered.connect(self.subject_ctrl.add_subject)
        self.ui.actionRemove_subject.triggered.connect(self.subject_ctrl.remove_subject)

        self.sort_filter_ctrl.reloadModelRequested.connect(self.task_ctrl.reload_model)
        self.task_ctrl.updateSortAndFilterRequested.connect(
            self.sort_filter_ctrl.reload_tasks
        )

        self.ui.filterByAllSubjectsCheckBox.setChecked(True)

    @Slot()
    def subject_added(self, subject: str):
        self.ui.filterBySubjectComboBox.addItem(subject)

        self.ui.filterBySubjectComboBox.adjustSize()
        self.ui.filterBySubjectComboBox.updateGeometry()


class SubjectItemController(QObject):
    subjectAdded = Signal(str)
    subjectRemoved = Signal(int)  # index

    def __init__(self, ctrl_parent: "TaskTodosController"):
        super().__init__(ctrl_parent)
        self.ctrl_parent = ctrl_parent
        self.mw_parent = ctrl_parent.mw_parent

        self.ui = ctrl_parent.ui
        self.app_data = ctrl_parent.app_data

    @Slot()
    def add_subject(self):
        text, ok = QInputDialog.getText(
            self.mw_parent, "Task to-dos - Add subject", "Enter subject name:"
        )
        if text in self.app_data.subjects:
            QMessageBox.warning(
                self.mw_parent,
                "Task to-dos - Add subject",
                "Provided subject already exists.",
            )
            return

        if text and ok:
            self.app_data.subjects.append(text)
            self.app_data.save_settings()

            self.subjectAdded.emit(text)

    @Slot()
    def remove_subject(self):
        if not self.app_data.subjects:
            QMessageBox.information(
                self.mw_parent,
                "Task to-dos - Remove subject",
                "There are no subjects to remove.",
            )
            return

        item, ok = QInputDialog.getItem(
            self.mw_parent,
            "Task to-dos - Remove subject",
            "Choose a subject to delete:",
            self.app_data.subjects,
        )
        if item and ok:
            self.subjectRemoved.emit(self.app_data.subjects.index(item))

            self.app_data.subjects.remove(item)
            self.app_data.save_settings()


class TasksItemController(QObject):
    updateSortAndFilterRequested = Signal()

    def __init__(self, ctrl_parent: "TaskTodosController"):
        super().__init__(ctrl_parent)
        self.ctrl_parent = ctrl_parent
        self.mw_parent = ctrl_parent.mw_parent

        self.ui = ctrl_parent.ui
        self.app_data = ctrl_parent.app_data

        self.task_dialog: TaskInfoDialog = TaskInfoDialog(self)
        self.model = TaskTodosTableModel(self)

        self.ui.tasksTableView.setModel(self.model)
        self.setup()

    def setup(self):
        self.task_dialog.addTaskRequested.connect(self.add_task_accepted)
        self.task_dialog.editTaskRequested.connect(self.edit_task_accepted)

        self.ui.tasksTableView.doubleClicked.connect(self.edit_task_triggered)

        self.ui.addTaskButton.clicked.connect(self.add_task_triggered)
        self.ui.removeTaskButton.clicked.connect(self.remove_task_triggered)
        self.ui.completeTaskButton.clicked.connect(self.complete_task_triggered)

        self.ui.actionAdd_task.triggered.connect(self.add_task_triggered)
        self.ui.actionRemove_task.triggered.connect(self.remove_task_triggered)

        self.ui.actionEdit_task.triggered.connect(self.edit_task_triggered)
        self.ui.actionMark_task_completed.triggered.connect(
            self.complete_task_triggered
        )

        self.model.load_tasks(self.app_data.tasks)

    @Slot(list)
    def reload_model(self, tasks: list[SubjectTask]):
        self.model.load_tasks(tasks)
        logger.info("Reloaded model")

    @Slot()
    def add_task_triggered(self):
        if not self.app_data.subjects:
            QMessageBox.warning(
                self.mw_parent,
                "Task to-dos - Add task",
                "No subjects have been defined yet, please create a subject for tasks.",
            )
            return

        self.task_dialog.reset_data(self.app_data.subjects)
        self.task_dialog.show()

    @Slot()
    def add_task_accepted(self, task: EditedSubjectTask):
        new_task = SubjectTask(
            task_id=uuid.uuid4(), completed=False, **task.model_dump()
        )
        self.app_data.tasks.append(new_task)

        self.app_data.save_settings()
        self.model.add_task(new_task)

        self.updateSortAndFilterRequested.emit()

    @Slot()
    def remove_task_triggered(self):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return

        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        btn = QMessageBox.information(
            self.mw_parent,
            "Task to-dos - Delete task",
            "Do you want to delete the currently selected task?",
            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            defaultButton=QMessageBox.StandardButton.No,
        )
        if btn == QMessageBox.StandardButton.No:
            return

        self.app_data.tasks.remove(data)
        self.app_data.save_settings()

        self.model.delete_task(index)
        self.updateSortAndFilterRequested.emit()

    @Slot()
    def complete_task_triggered(self):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return

        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        new_model = data.model_copy()
        new_model.completed = not new_model.completed

        data_index = self.app_data.tasks.index(data)
        self.app_data.tasks[data_index] = new_model

        self.app_data.save_settings()
        self.model.update_task(index, new_model)

        if not data.completed:
            QMessageBox.information(
                self.mw_parent,
                "Task to-dos - Add task",
                f"Task '{new_model.task}' successfully completed!",
            )

    @Slot()
    def edit_task_triggered(self):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return

        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        self.task_dialog.reset_data(
            self.app_data.subjects, emit_as=EmitDialogInfoAs.edit
        )
        self.task_dialog.set_existing_data(data)

        self.task_dialog.show()

    @Slot(EditedTaskWithID)
    def edit_task_accepted(self, task: EditedTaskWithID):
        indexes = self.ui.tasksTableView.selectedIndexes()
        if not indexes:
            return

        index = indexes[0]
        data: SubjectTask = index.data(Qt.ItemDataRole.UserRole)

        edited_task = SubjectTask(
            subject=task.subject,
            deadline=task.deadline,
            task=task.task,
            completed=task.completed,
            task_id=task.task_id,
        )

        data_index = self.app_data.tasks.index(data)
        self.app_data.tasks[data_index] = edited_task

        self.app_data.save_settings()
        self.model.update_task(index, edited_task)

        self.updateSortAndFilterRequested.emit()


class SortAndFilterController(QObject):
    reloadModelRequested = Signal(list)  # list[SubjectTask]

    def __init__(self, ctrl_parent: "TaskTodosController"):
        super().__init__(ctrl_parent)
        self.ctrl_parent = ctrl_parent
        self.mw_parent = ctrl_parent.mw_parent

        self.ui = ctrl_parent.ui
        self.app_data = ctrl_parent.app_data

        self._sort_filter_state: SortAndFilterState = SortAndFilterState()
        self.setup()

    def setup(self):
        self.ui.filterBySubjectComboBox.currentIndexChanged.connect(
            self.change_subject_filter
        )
        self.ui.filterByAllSubjectsCheckBox.toggled.connect(
            self.filter_all_subjects_toggled
        )

        self.ui.sortByComboBox.currentIndexChanged.connect(self.change_sorting_rule)

    @Slot(bool)
    def filter_all_subjects_toggled(self, checked: bool):
        if checked:
            self._sort_filter_state.include_all_subjects = True
            self._sort_filter_state.subject_filter = None

            self.ui.filterBySubjectComboBox.setEnabled(False)
        else:
            subject_idx = self.ui.filterBySubjectComboBox.currentIndex()
            if subject_idx != -1:
                subject: str = self.app_data.subjects[subject_idx]
            else:
                subject: None = None

            self._sort_filter_state.subject_filter = subject
            self._sort_filter_state.include_all_subjects = False

            self.ui.filterBySubjectComboBox.setEnabled(True)

        self._emit_tasks()

    @Slot(int)
    def change_subject_filter(self, subject_idx: int):
        subject: str = self.app_data.subjects[subject_idx]
        self._sort_filter_state.subject_filter = subject

        self._emit_tasks()

    @Slot(int)
    def change_sorting_rule(self, index: int):
        self._sort_filter_state.sort_filter = index
        self._emit_tasks()

    @Slot()
    def reload_tasks(self):
        self._emit_tasks()

    def _emit_tasks(self):
        state = self._sort_filter_state

        if not state.include_all_subjects and state.subject_filter is not None:
            tasks = self._get_tasks_by_subject(state.subject_filter)
        else:
            tasks = self.app_data.tasks

        match self._sort_filter_state.sort_filter:
            case SortByComboBoxEnum.closest_to_deadline:
                tasks_sorted = sorted(tasks, key=lambda task: task.deadline)
            case SortByComboBoxEnum.farthest_to_deadline:
                tasks_sorted = sorted(
                    tasks, key=lambda task: task.deadline, reverse=True
                )
            case SortByComboBoxEnum.subjects_a_to_z:
                tasks_sorted = sorted(tasks, key=lambda task: task.subject)

        self.reloadModelRequested.emit(tasks_sorted)

    def _get_tasks_by_subject(self, subject: str):
        tasks: list[SubjectTask] = []

        for task in self.app_data.tasks:
            if task.subject != subject:
                continue
            tasks.append(task)

        return tasks


class TaskInfoDialog(QDialog):
    addTaskRequested = Signal(EditedSubjectTask)
    editTaskRequested = Signal(EditedTaskWithID)

    def __init__(self, /, parent: TaskTodosController):
        super().__init__(parent.mw_parent)
        self.ui = Ui_AddTaskDialog()

        self.todo_parent = parent

        self._emit_as: EmitDialogInfoAs = None
        self._data: SubjectTask | None = None

        self.ui.setupUi(self)

    def reset_data(
        self, subjects: list[str], emit_as: EmitDialogInfoAs = EmitDialogInfoAs.add
    ):
        self._emit_as = emit_as
        self._data = None

        self.ui.subjectComboBox.clear()
        self.ui.subjectComboBox.addItems(subjects)

        self.ui.deadlineDateTimeEdit.setDateTime(QDateTime.currentDateTimeUtc())
        self.ui.taskPlainTextEdit.setPlainText("")

    def set_existing_data(self, data: SubjectTask):
        py_date = data.deadline.timestamp()
        qt_date = QDateTime.fromSecsSinceEpoch(int(py_date), Qt.TimeSpec.UTC)

        self.ui.deadlineDateTimeEdit.setDateTime(qt_date)
        self.ui.taskPlainTextEdit.setPlainText(data.task)

        self.ui.subjectComboBox.setCurrentText(data.subject)
        self._data = data

    def accept(self):
        task = self.ui.taskPlainTextEdit.toPlainText()
        subject = self.ui.subjectComboBox.currentText()

        qt_deadline = self.ui.deadlineDateTimeEdit.dateTime()
        py_deadline: datetime = qt_deadline.toPython()

        aware_deadline: datetime = py_deadline.astimezone(timezone.utc)
        data = EditedSubjectTask(subject=subject, deadline=aware_deadline, task=task)

        if self._emit_as == EmitDialogInfoAs.add:
            self.addTaskRequested.emit(data)
        elif self._emit_as == EmitDialogInfoAs.edit:
            assert self._data is not None, "Edit data is invalid"

            with_id_data = EditedTaskWithID(
                task_id=self._data.task_id,
                completed=self._data.completed,
                **data.model_dump(),
            )
            self.editTaskRequested.emit(with_id_data)

        return super().accept()
