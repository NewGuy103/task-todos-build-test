# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_task_dialog.ui'
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
    QAbstractButton,
    QApplication,
    QComboBox,
    QDateTimeEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QFrame,
    QLabel,
    QPlainTextEdit,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class Ui_AddTaskDialog(object):
    def setupUi(self, AddTaskDialog):
        if not AddTaskDialog.objectName():
            AddTaskDialog.setObjectName("AddTaskDialog")
        AddTaskDialog.setWindowModality(Qt.WindowModality.WindowModal)
        AddTaskDialog.resize(400, 300)
        self.verticalLayout = QVBoxLayout(AddTaskDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainDialogFrame = QFrame(AddTaskDialog)
        self.mainDialogFrame.setObjectName("mainDialogFrame")
        self.mainDialogFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainDialogFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainDialogFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.subjectLabel = QLabel(self.mainDialogFrame)
        self.subjectLabel.setObjectName("subjectLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.subjectLabel)

        self.subjectComboBox = QComboBox(self.mainDialogFrame)
        self.subjectComboBox.setObjectName("subjectComboBox")

        self.formLayout.setWidget(
            0, QFormLayout.ItemRole.FieldRole, self.subjectComboBox
        )

        self.deadlineLabel = QLabel(self.mainDialogFrame)
        self.deadlineLabel.setObjectName("deadlineLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.deadlineLabel)

        self.deadlineDateTimeEdit = QDateTimeEdit(self.mainDialogFrame)
        self.deadlineDateTimeEdit.setObjectName("deadlineDateTimeEdit")

        self.formLayout.setWidget(
            1, QFormLayout.ItemRole.FieldRole, self.deadlineDateTimeEdit
        )

        self.taskLabel = QLabel(self.mainDialogFrame)
        self.taskLabel.setObjectName("taskLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.taskLabel)

        self.taskPlainTextEdit = QPlainTextEdit(self.mainDialogFrame)
        self.taskPlainTextEdit.setObjectName("taskPlainTextEdit")

        self.formLayout.setWidget(
            2, QFormLayout.ItemRole.FieldRole, self.taskPlainTextEdit
        )

        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalLayout.addWidget(self.mainDialogFrame)

        self.dialogButtonBox = QDialogButtonBox(AddTaskDialog)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.dialogButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.dialogButtonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )

        self.verticalLayout.addWidget(self.dialogButtonBox)

        self.retranslateUi(AddTaskDialog)
        self.dialogButtonBox.accepted.connect(AddTaskDialog.accept)
        self.dialogButtonBox.rejected.connect(AddTaskDialog.reject)

        QMetaObject.connectSlotsByName(AddTaskDialog)

    # setupUi

    def retranslateUi(self, AddTaskDialog):
        AddTaskDialog.setWindowTitle(
            QCoreApplication.translate("AddTaskDialog", "Task to-dos - Add task", None)
        )
        self.subjectLabel.setText(
            QCoreApplication.translate("AddTaskDialog", "Subject:", None)
        )
        self.deadlineLabel.setText(
            QCoreApplication.translate("AddTaskDialog", "Deadline:", None)
        )
        self.deadlineDateTimeEdit.setDisplayFormat(
            QCoreApplication.translate("AddTaskDialog", "M/d/yy h:mm:ss\u202fAp", None)
        )
        self.taskLabel.setText(
            QCoreApplication.translate("AddTaskDialog", "Task:", None)
        )

    # retranslateUi
