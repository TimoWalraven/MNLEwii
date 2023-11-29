# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'STEP_V0.1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

from widgets import (ApMl, Stabilogram)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 1000)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QSize(50, 50))
        MainWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.modes = QTabWidget(self.centralwidget)
        self.modes.setObjectName(u"modes")
        self.modes.setStyleSheet(u"")
        self.livetab = QWidget()
        self.livetab.setObjectName(u"livetab")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.livetab.sizePolicy().hasHeightForWidth())
        self.livetab.setSizePolicy(sizePolicy1)
        self.verticalLayout_5 = QVBoxLayout(self.livetab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.statuslight = QPushButton(self.livetab)
        self.statuslight.setObjectName(u"statuslight")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.statuslight.sizePolicy().hasHeightForWidth())
        self.statuslight.setSizePolicy(sizePolicy2)
        self.statuslight.setMinimumSize(QSize(20, 20))
        self.statuslight.setMaximumSize(QSize(20, 20))
        self.statuslight.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px; ")

        self.horizontalLayout.addWidget(self.statuslight)

        self.comport = QComboBox(self.livetab)
        self.comport.setObjectName(u"comport")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comport.sizePolicy().hasHeightForWidth())
        self.comport.setSizePolicy(sizePolicy3)
        self.comport.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.comport)

        self.label = QLabel(self.livetab)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.statustext = QLabel(self.livetab)
        self.statustext.setObjectName(u"statustext")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.statustext.sizePolicy().hasHeightForWidth())
        self.statustext.setSizePolicy(sizePolicy4)
        self.statustext.setFrameShape(QFrame.Box)

        self.horizontalLayout.addWidget(self.statustext)

        self.recordlength = QSpinBox(self.livetab)
        self.recordlength.setObjectName(u"recordlength")
        self.recordlength.setMinimum(1)
        self.recordlength.setMaximum(120)
        self.recordlength.setValue(30)

        self.horizontalLayout.addWidget(self.recordlength)

        self.startrecording = QPushButton(self.livetab)
        self.startrecording.setObjectName(u"startrecording")

        self.horizontalLayout.addWidget(self.startrecording)

        self.analyserecording = QPushButton(self.livetab)
        self.analyserecording.setObjectName(u"analyserecording")
        self.analyserecording.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.analyserecording)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.datadisplay = QHBoxLayout()
        self.datadisplay.setObjectName(u"datadisplay")
        self.livestabilogramwidget = Stabilogram(self.livetab)
        self.livestabilogramwidget.setObjectName(u"livestabilogramwidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.livestabilogramwidget.sizePolicy().hasHeightForWidth())
        self.livestabilogramwidget.setSizePolicy(sizePolicy5)
        self.livestabilogramwidget.setMinimumSize(QSize(800, 800))
        self.livestabilogramwidget.setStyleSheet(u"")

        self.datadisplay.addWidget(self.livestabilogramwidget)

        self.livedisplayright = QVBoxLayout()
        self.livedisplayright.setObjectName(u"livedisplayright")
        self.frame = QFrame(self.livetab)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 300))
        self.frame.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.stancelabel = QLabel(self.frame)
        self.stancelabel.setObjectName(u"stancelabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.stancelabel)

        self.stanceselect = QComboBox(self.frame)
        self.stanceselect.addItem("")
        self.stanceselect.addItem("")
        self.stanceselect.addItem("")
        self.stanceselect.addItem("")
        self.stanceselect.setObjectName(u"stanceselect")
        self.stanceselect.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.stanceselect)

        self.eyelabel = QLabel(self.frame)
        self.eyelabel.setObjectName(u"eyelabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.eyelabel)

        self.eyeselect = QComboBox(self.frame)
        self.eyeselect.addItem("")
        self.eyeselect.addItem("")
        self.eyeselect.setObjectName(u"eyeselect")
        self.eyeselect.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.eyeselect)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.line)

        self.patientinfolabel = QLabel(self.frame)
        self.patientinfolabel.setObjectName(u"patientinfolabel")
        self.patientinfolabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.patientinfolabel)

        self.agelabel = QLabel(self.frame)
        self.agelabel.setObjectName(u"agelabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.agelabel)

        self.ageselect = QSpinBox(self.frame)
        self.ageselect.setObjectName(u"ageselect")
        self.ageselect.setMaximum(130)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.ageselect)

        self.heightlabel = QLabel(self.frame)
        self.heightlabel.setObjectName(u"heightlabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.heightlabel)

        self.heightselect = QSpinBox(self.frame)
        self.heightselect.setObjectName(u"heightselect")
        self.heightselect.setMaximum(260)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.heightselect)

        self.weightlabel = QLabel(self.frame)
        self.weightlabel.setObjectName(u"weightlabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.weightlabel)

        self.weightselect = QSpinBox(self.frame)
        self.weightselect.setObjectName(u"weightselect")
        self.weightselect.setMaximum(1000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.weightselect)

        self.commentlabel = QLabel(self.frame)
        self.commentlabel.setObjectName(u"commentlabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.commentlabel)

        self.commentedit = QPlainTextEdit(self.frame)
        self.commentedit.setObjectName(u"commentedit")
        sizePolicy5.setHeightForWidth(self.commentedit.sizePolicy().hasHeightForWidth())
        self.commentedit.setSizePolicy(sizePolicy5)
        self.commentedit.setMinimumSize(QSize(100, 50))

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.commentedit)

        self.conditionlabel = QLabel(self.frame)
        self.conditionlabel.setObjectName(u"conditionlabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.conditionlabel)

        self.conditionselect = QComboBox(self.frame)
        self.conditionselect.addItem("")
        self.conditionselect.addItem("")
        self.conditionselect.addItem("")
        self.conditionselect.setObjectName(u"conditionselect")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.conditionselect)

        self.testinfolabel = QLabel(self.frame)
        self.testinfolabel.setObjectName(u"testinfolabel")
        self.testinfolabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.testinfolabel)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.livedisplayright.addWidget(self.frame)

        self.liveapwidget = ApMl(self.livetab)
        self.liveapwidget.setObjectName(u"liveapwidget")
        sizePolicy5.setHeightForWidth(self.liveapwidget.sizePolicy().hasHeightForWidth())
        self.liveapwidget.setSizePolicy(sizePolicy5)
        self.liveapwidget.setMinimumSize(QSize(400, 200))
        self.liveapwidget.setStyleSheet(u"")

        self.livedisplayright.addWidget(self.liveapwidget)

        self.livemlwidget = ApMl(self.livetab)
        self.livemlwidget.setObjectName(u"livemlwidget")
        sizePolicy5.setHeightForWidth(self.livemlwidget.sizePolicy().hasHeightForWidth())
        self.livemlwidget.setSizePolicy(sizePolicy5)
        self.livemlwidget.setMinimumSize(QSize(400, 200))
        self.livemlwidget.setStyleSheet(u"")

        self.livedisplayright.addWidget(self.livemlwidget)


        self.datadisplay.addLayout(self.livedisplayright)

        self.datadisplay.setStretch(0, 3)
        self.datadisplay.setStretch(1, 2)

        self.verticalLayout_5.addLayout(self.datadisplay)

        self.verticalLayout_5.setStretch(1, 1)
        self.modes.addTab(self.livetab, "")
        self.analysistab = QWidget()
        self.analysistab.setObjectName(u"analysistab")
        self.verticalLayout_2 = QVBoxLayout(self.analysistab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.analysistoolbar = QHBoxLayout()
        self.analysistoolbar.setObjectName(u"analysistoolbar")
        self.analysisopenfile = QPushButton(self.analysistab)
        self.analysisopenfile.setObjectName(u"analysisopenfile")

        self.analysistoolbar.addWidget(self.analysisopenfile)

        self.analysisplay = QPushButton(self.analysistab)
        self.analysisplay.setObjectName(u"analysisplay")

        self.analysistoolbar.addWidget(self.analysisplay)

        self.currenttime = QLabel(self.analysistab)
        self.currenttime.setObjectName(u"currenttime")
        self.currenttime.setMinimumSize(QSize(30, 0))
        self.currenttime.setAlignment(Qt.AlignCenter)

        self.analysistoolbar.addWidget(self.currenttime)

        self.timeslider = QSlider(self.analysistab)
        self.timeslider.setObjectName(u"timeslider")
        self.timeslider.setOrientation(Qt.Horizontal)

        self.analysistoolbar.addWidget(self.timeslider)

        self.maxtime = QLabel(self.analysistab)
        self.maxtime.setObjectName(u"maxtime")
        self.maxtime.setMinimumSize(QSize(30, 0))
        self.maxtime.setAlignment(Qt.AlignCenter)

        self.analysistoolbar.addWidget(self.maxtime)

        self.analysisrestart = QPushButton(self.analysistab)
        self.analysisrestart.setObjectName(u"analysisrestart")

        self.analysistoolbar.addWidget(self.analysisrestart)

        self.saverecording = QPushButton(self.analysistab)
        self.saverecording.setObjectName(u"saverecording")

        self.analysistoolbar.addWidget(self.saverecording)

        self.viewselection = QPushButton(self.analysistab)
        self.viewselection.setObjectName(u"viewselection")

        self.analysistoolbar.addWidget(self.viewselection)


        self.verticalLayout_2.addLayout(self.analysistoolbar)

        self.analysisscrollarea = QScrollArea(self.analysistab)
        self.analysisscrollarea.setObjectName(u"analysisscrollarea")
        self.analysisscrollarea.setWidgetResizable(True)
        self.analysiswidgetarea = QWidget()
        self.analysiswidgetarea.setObjectName(u"analysiswidgetarea")
        self.analysiswidgetarea.setGeometry(QRect(0, 0, 1548, 888))
        self.verticalLayout_3 = QVBoxLayout(self.analysiswidgetarea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.analysiswidgetgrid = QGridLayout()
        self.analysiswidgetgrid.setObjectName(u"analysiswidgetgrid")
        self.widget_4 = QWidget(self.analysiswidgetarea)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"background-color: rgb(191, 191, 191);\n"
"border-color: rgb(0, 0, 0);")

        self.analysiswidgetgrid.addWidget(self.widget_4, 1, 1, 1, 1)

        self.widget_2 = QWidget(self.analysiswidgetarea)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 400))
        self.widget_2.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-thickness: 1px;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tableWidget = QTableWidget(self.widget_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout_3.addWidget(self.tableWidget)


        self.analysiswidgetgrid.addWidget(self.widget_2, 1, 0, 1, 1)

        self.widget = Stabilogram(self.analysiswidgetarea)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 400))
        self.widget.setStyleSheet(u"background-color: rgb(207, 207, 207);\n"
"border-color: rgb(0, 0, 0);")

        self.analysiswidgetgrid.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalWidget = QWidget(self.analysiswidgetarea)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.verticalWidget.setMinimumSize(QSize(400, 200))
        self.verticalLayout_4 = QVBoxLayout(self.verticalWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.analysisapwidget = ApMl(self.verticalWidget)
        self.analysisapwidget.setObjectName(u"analysisapwidget")
        self.analysisapwidget.setMinimumSize(QSize(400, 200))

        self.verticalLayout_4.addWidget(self.analysisapwidget)

        self.analysismlwidget = ApMl(self.verticalWidget)
        self.analysismlwidget.setObjectName(u"analysismlwidget")
        self.analysismlwidget.setMinimumSize(QSize(400, 200))

        self.verticalLayout_4.addWidget(self.analysismlwidget)


        self.analysiswidgetgrid.addWidget(self.verticalWidget, 0, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.analysiswidgetgrid)

        self.analysisscrollarea.setWidget(self.analysiswidgetarea)

        self.verticalLayout_2.addWidget(self.analysisscrollarea)

        self.verticalLayout_2.setStretch(1, 1)
        self.modes.addTab(self.analysistab, "")

        self.verticalLayout.addWidget(self.modes)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.modes.setCurrentIndex(1)
        self.stanceselect.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"STEP", None))
        self.statuslight.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.statustext.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.recordlength.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.startrecording.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.analyserecording.setText(QCoreApplication.translate("MainWindow", u"Analyse recording ->", None))
        self.stancelabel.setText(QCoreApplication.translate("MainWindow", u"Stance", None))
        self.stanceselect.setItemText(0, QCoreApplication.translate("MainWindow", u"double legged", None))
        self.stanceselect.setItemText(1, QCoreApplication.translate("MainWindow", u"left leg", None))
        self.stanceselect.setItemText(2, QCoreApplication.translate("MainWindow", u"right leg", None))
        self.stanceselect.setItemText(3, QCoreApplication.translate("MainWindow", u"tandem", None))

        self.stanceselect.setCurrentText(QCoreApplication.translate("MainWindow", u"double legged", None))
        self.eyelabel.setText(QCoreApplication.translate("MainWindow", u"Eyes", None))
        self.eyeselect.setItemText(0, QCoreApplication.translate("MainWindow", u"open", None))
        self.eyeselect.setItemText(1, QCoreApplication.translate("MainWindow", u"closed", None))

        self.eyeselect.setCurrentText(QCoreApplication.translate("MainWindow", u"open", None))
        self.patientinfolabel.setText(QCoreApplication.translate("MainWindow", u"Patient info", None))
        self.agelabel.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.heightlabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.heightselect.setSuffix(QCoreApplication.translate("MainWindow", u" (cm)", None))
        self.weightlabel.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.weightselect.setSuffix(QCoreApplication.translate("MainWindow", u" (Kg)", None))
        self.commentlabel.setText(QCoreApplication.translate("MainWindow", u"Comments", None))
        self.conditionlabel.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.conditionselect.setItemText(0, QCoreApplication.translate("MainWindow", u"Healthy", None))
        self.conditionselect.setItemText(1, QCoreApplication.translate("MainWindow", u"Parkinsons", None))
        self.conditionselect.setItemText(2, QCoreApplication.translate("MainWindow", u"Stroke", None))

        self.testinfolabel.setText(QCoreApplication.translate("MainWindow", u"Test info", None))
        self.modes.setTabText(self.modes.indexOf(self.livetab), QCoreApplication.translate("MainWindow", u"Live", None))
        self.analysisopenfile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.analysisplay.setText(QCoreApplication.translate("MainWindow", u"\u23ef\ufe0f", None))
        self.currenttime.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.maxtime.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.analysisrestart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.saverecording.setText(QCoreApplication.translate("MainWindow", u"Save report", None))
        self.viewselection.setText(QCoreApplication.translate("MainWindow", u"Views", None))
        self.modes.setTabText(self.modes.indexOf(self.analysistab), QCoreApplication.translate("MainWindow", u"Analysis", None))
    # retranslateUi

