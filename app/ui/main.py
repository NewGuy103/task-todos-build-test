# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QCheckBox,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QStatusBar,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.actionAdd_task = QAction(MainWindow)
        self.actionAdd_task.setObjectName("actionAdd_task")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.actionAdd_task.setIcon(icon)
        self.actionRemove_task = QAction(MainWindow)
        self.actionRemove_task.setObjectName("actionRemove_task")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListRemove))
        self.actionRemove_task.setIcon(icon1)
        self.actionAdd_subject = QAction(MainWindow)
        self.actionAdd_subject.setObjectName("actionAdd_subject")
        self.actionAdd_subject.setIcon(icon)
        self.actionRemove_subject = QAction(MainWindow)
        self.actionRemove_subject.setObjectName("actionRemove_subject")
        self.actionRemove_subject.setIcon(icon1)
        self.actionHow_to_use = QAction(MainWindow)
        self.actionHow_to_use.setObjectName("actionHow_to_use")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        self.actionHow_to_use.setIcon(icon2)
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionMark_task_completed = QAction(MainWindow)
        self.actionMark_task_completed.setObjectName("actionMark_task_completed")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoUp))
        self.actionMark_task_completed.setIcon(icon3)
        self.actionEdit_task = QAction(MainWindow)
        self.actionEdit_task.setObjectName("actionEdit_task")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.actionEdit_task.setIcon(icon4)
        self.actionSource_code = QAction(MainWindow)
        self.actionSource_code.setObjectName("actionSource_code")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpAbout))
        self.actionSource_code.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainStackedWidget = QStackedWidget(self.centralwidget)
        self.mainStackedWidget.setObjectName("mainStackedWidget")
        self.mainPage = QWidget()
        self.mainPage.setObjectName("mainPage")
        self.verticalLayout_2 = QVBoxLayout(self.mainPage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tasksLabel = QLabel(self.mainPage)
        self.tasksLabel.setObjectName("tasksLabel")
        font = QFont()
        font.setPointSize(12)
        self.tasksLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.tasksLabel)

        self.sortAndFilterFrame = QFrame(self.mainPage)
        self.sortAndFilterFrame.setObjectName("sortAndFilterFrame")
        self.sortAndFilterFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sortAndFilterFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.sortAndFilterFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 6, 0, 6)
        self.sortByWidget = QWidget(self.sortAndFilterFrame)
        self.sortByWidget.setObjectName("sortByWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.sortByWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.sortByLabel = QLabel(self.sortByWidget)
        self.sortByLabel.setObjectName("sortByLabel")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sortByLabel.sizePolicy().hasHeightForWidth())
        self.sortByLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.sortByLabel)

        self.sortByComboBox = QComboBox(self.sortByWidget)
        self.sortByComboBox.addItem("")
        self.sortByComboBox.addItem("")
        self.sortByComboBox.addItem("")
        self.sortByComboBox.setObjectName("sortByComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.sortByComboBox.sizePolicy().hasHeightForWidth()
        )
        self.sortByComboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.sortByComboBox)

        self.horizontalLayout_2.addWidget(self.sortByWidget)

        self.filterBySubjectWidget = QWidget(self.sortAndFilterFrame)
        self.filterBySubjectWidget.setObjectName("filterBySubjectWidget")
        self.horizontalLayout_4 = QHBoxLayout(self.filterBySubjectWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.filterBySubjectLabel = QLabel(self.filterBySubjectWidget)
        self.filterBySubjectLabel.setObjectName("filterBySubjectLabel")
        sizePolicy.setHeightForWidth(
            self.filterBySubjectLabel.sizePolicy().hasHeightForWidth()
        )
        self.filterBySubjectLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.filterBySubjectLabel)

        self.filterBySubjectComboBox = QComboBox(self.filterBySubjectWidget)
        self.filterBySubjectComboBox.setObjectName("filterBySubjectComboBox")
        sizePolicy1.setHeightForWidth(
            self.filterBySubjectComboBox.sizePolicy().hasHeightForWidth()
        )
        self.filterBySubjectComboBox.setSizePolicy(sizePolicy1)
        self.filterBySubjectComboBox.setSizeAdjustPolicy(
            QComboBox.SizeAdjustPolicy.AdjustToContents
        )

        self.horizontalLayout_4.addWidget(self.filterBySubjectComboBox)

        self.filterByAllSubjectsCheckBox = QCheckBox(self.filterBySubjectWidget)
        self.filterByAllSubjectsCheckBox.setObjectName("filterByAllSubjectsCheckBox")

        self.horizontalLayout_4.addWidget(self.filterByAllSubjectsCheckBox)

        self.horizontalLayout_2.addWidget(self.filterBySubjectWidget)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout_2.addWidget(self.sortAndFilterFrame)

        self.tasksTableView = QTableView(self.mainPage)
        self.tasksTableView.setObjectName("tasksTableView")
        self.tasksTableView.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.tasksTableView.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.tasksTableView.setTextElideMode(Qt.TextElideMode.ElideNone)
        self.tasksTableView.setGridStyle(Qt.PenStyle.NoPen)

        self.verticalLayout_2.addWidget(self.tasksTableView)

        self.taskOptionsFrame = QFrame(self.mainPage)
        self.taskOptionsFrame.setObjectName("taskOptionsFrame")
        self.taskOptionsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.taskOptionsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.taskOptionsFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addTaskButton = QPushButton(self.taskOptionsFrame)
        self.addTaskButton.setObjectName("addTaskButton")
        self.addTaskButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.addTaskButton)

        self.removeTaskButton = QPushButton(self.taskOptionsFrame)
        self.removeTaskButton.setObjectName("removeTaskButton")
        self.removeTaskButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.removeTaskButton)

        self.completeTaskButton = QPushButton(self.taskOptionsFrame)
        self.completeTaskButton.setObjectName("completeTaskButton")
        self.completeTaskButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.completeTaskButton)

        self.verticalLayout_2.addWidget(self.taskOptionsFrame)

        self.mainStackedWidget.addWidget(self.mainPage)

        self.verticalLayout.addWidget(self.mainStackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 20))
        self.menuDeadlines = QMenu(self.menubar)
        self.menuDeadlines.setObjectName("menuDeadlines")
        self.menuSubject = QMenu(self.menubar)
        self.menuSubject.setObjectName("menuSubject")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuDeadlines.menuAction())
        self.menubar.addAction(self.menuSubject.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuDeadlines.addAction(self.actionAdd_task)
        self.menuDeadlines.addAction(self.actionRemove_task)
        self.menuDeadlines.addAction(self.actionEdit_task)
        self.menuDeadlines.addAction(self.actionMark_task_completed)
        self.menuSubject.addAction(self.actionAdd_subject)
        self.menuSubject.addAction(self.actionRemove_subject)
        self.menuHelp.addAction(self.actionHow_to_use)
        self.menuHelp.addAction(self.actionSource_code)

        self.retranslateUi(MainWindow)

        self.mainStackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Task To-dos", None)
        )
        self.actionAdd_task.setText(
            QCoreApplication.translate("MainWindow", "Add task", None)
        )
        self.actionRemove_task.setText(
            QCoreApplication.translate("MainWindow", "Remove task", None)
        )
        self.actionAdd_subject.setText(
            QCoreApplication.translate("MainWindow", "Add subject", None)
        )
        self.actionRemove_subject.setText(
            QCoreApplication.translate("MainWindow", "Remove subject", None)
        )
        self.actionHow_to_use.setText(
            QCoreApplication.translate("MainWindow", "How to use", None)
        )
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", "About", None)
        )
        self.actionMark_task_completed.setText(
            QCoreApplication.translate("MainWindow", "Mark task completed", None)
        )
        self.actionEdit_task.setText(
            QCoreApplication.translate("MainWindow", "Edit task", None)
        )
        self.actionSource_code.setText(
            QCoreApplication.translate("MainWindow", "Source code", None)
        )
        self.tasksLabel.setText(
            QCoreApplication.translate("MainWindow", "Upcoming tasks:", None)
        )
        self.sortByLabel.setText(
            QCoreApplication.translate("MainWindow", "Sort by:", None)
        )
        self.sortByComboBox.setItemText(
            0, QCoreApplication.translate("MainWindow", "Closest to deadline", None)
        )
        self.sortByComboBox.setItemText(
            1, QCoreApplication.translate("MainWindow", "Farthest to deadline", None)
        )
        self.sortByComboBox.setItemText(
            2, QCoreApplication.translate("MainWindow", "Subjects - A-Z", None)
        )

        self.filterBySubjectLabel.setText(
            QCoreApplication.translate("MainWindow", "Filter subjects:", None)
        )
        self.filterByAllSubjectsCheckBox.setText(
            QCoreApplication.translate("MainWindow", "All subjects", None)
        )
        self.addTaskButton.setText(
            QCoreApplication.translate("MainWindow", "Add task", None)
        )
        self.removeTaskButton.setText(
            QCoreApplication.translate("MainWindow", "Remove task", None)
        )
        self.completeTaskButton.setText(
            QCoreApplication.translate("MainWindow", "Mark task completed", None)
        )
        self.menuDeadlines.setTitle(
            QCoreApplication.translate("MainWindow", "Tasks", None)
        )
        self.menuSubject.setTitle(
            QCoreApplication.translate("MainWindow", "Subjects", None)
        )
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
