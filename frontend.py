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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSlider, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from widgets import (ApMl, Stabilogram)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1252, 896)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../../../../Stichting Hogeschool Utrecht/Wii balance board - General/Pictures/STEP-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.recordlength.setMinimum(11)
        self.recordlength.setMaximum(120)
        self.recordlength.setValue(30)

        self.horizontalLayout.addWidget(self.recordlength)

        self.startrecording = QPushButton(self.livetab)
        self.startrecording.setObjectName(u"startrecording")
        font = QFont()
        font.setKerning(False)
        self.startrecording.setFont(font)
        self.startrecording.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.startrecording)

        self.analyserecording = QPushButton(self.livetab)
        self.analyserecording.setObjectName(u"analyserecording")
        self.analyserecording.setMinimumSize(QSize(150, 0))
        font1 = QFont()
        font1.setBold(False)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.analyserecording.setFont(font1)
        self.analyserecording.setFocusPolicy(Qt.StrongFocus)
        self.analyserecording.setContextMenuPolicy(Qt.DefaultContextMenu)

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
        sizePolicy5.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy5)
        self.frame.setMinimumSize(QSize(400, 400))
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
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.stancelabel = QLabel(self.frame)
        self.stancelabel.setObjectName(u"stancelabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.stancelabel)

        self.stanceselect = QComboBox(self.frame)
        self.stanceselect.addItem("")
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

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.agelabel)

        self.ageselect = QSpinBox(self.frame)
        self.ageselect.setObjectName(u"ageselect")
        self.ageselect.setMaximum(130)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.ageselect)

        self.heightlabel = QLabel(self.frame)
        self.heightlabel.setObjectName(u"heightlabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.heightlabel)

        self.heightselect = QSpinBox(self.frame)
        self.heightselect.setObjectName(u"heightselect")
        self.heightselect.setMaximum(260)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.heightselect)

        self.weightlabel = QLabel(self.frame)
        self.weightlabel.setObjectName(u"weightlabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.weightlabel)

        self.weightselect = QSpinBox(self.frame)
        self.weightselect.setObjectName(u"weightselect")
        self.weightselect.setMaximum(1000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.weightselect)

        self.commentlabel = QLabel(self.frame)
        self.commentlabel.setObjectName(u"commentlabel")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.commentlabel)

        self.notesedit = QPlainTextEdit(self.frame)
        self.notesedit.setObjectName(u"notesedit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.notesedit.sizePolicy().hasHeightForWidth())
        self.notesedit.setSizePolicy(sizePolicy6)
        self.notesedit.setMinimumSize(QSize(100, 30))
        self.notesedit.setMaximumSize(QSize(16777215, 100))

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.notesedit)

        self.conditionlabel = QLabel(self.frame)
        self.conditionlabel.setObjectName(u"conditionlabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.conditionlabel)

        self.conditionselect = QComboBox(self.frame)
        self.conditionselect.addItem("")
        self.conditionselect.addItem("")
        self.conditionselect.addItem("")
        self.conditionselect.addItem("")
        self.conditionselect.setObjectName(u"conditionselect")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.conditionselect)

        self.testinfolabel = QLabel(self.frame)
        self.testinfolabel.setObjectName(u"testinfolabel")
        self.testinfolabel.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.testinfolabel)

        self.medicationlabel = QLabel(self.frame)
        self.medicationlabel.setObjectName(u"medicationlabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.medicationlabel)

        self.medicationselect = QComboBox(self.frame)
        self.medicationselect.addItem("")
        self.medicationselect.addItem("")
        self.medicationselect.setObjectName(u"medicationselect")
        self.medicationselect.setEditable(True)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.medicationselect)

        self.fallhistorylabel = QLabel(self.frame)
        self.fallhistorylabel.setObjectName(u"fallhistorylabel")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.fallhistorylabel)

        self.fallhistoryselect = QComboBox(self.frame)
        self.fallhistoryselect.addItem("")
        self.fallhistoryselect.addItem("")
        self.fallhistoryselect.addItem("")
        self.fallhistoryselect.setObjectName(u"fallhistoryselect")
        self.fallhistoryselect.setEditable(True)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.fallhistoryselect)

        self.identifierlabel = QLabel(self.frame)
        self.identifierlabel.setObjectName(u"identifierlabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.identifierlabel)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.identifierselect = QLineEdit(self.frame)
        self.identifierselect.setObjectName(u"identifierselect")

        self.horizontalLayout_5.addWidget(self.identifierselect)

        self.identifierreload = QPushButton(self.frame)
        self.identifierreload.setObjectName(u"identifierreload")
        sizePolicy5.setHeightForWidth(self.identifierreload.sizePolicy().hasHeightForWidth())
        self.identifierreload.setSizePolicy(sizePolicy5)
        self.identifierreload.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_5.addWidget(self.identifierreload)


        self.formLayout.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_5)


        self.horizontalLayout_2.addLayout(self.formLayout)


        self.livedisplayright.addWidget(self.frame)

        self.liveapwidget = ApMl(self.livetab)
        self.liveapwidget.setObjectName(u"liveapwidget")
        sizePolicy.setHeightForWidth(self.liveapwidget.sizePolicy().hasHeightForWidth())
        self.liveapwidget.setSizePolicy(sizePolicy)
        self.liveapwidget.setMinimumSize(QSize(400, 160))
        self.liveapwidget.setStyleSheet(u"")

        self.livedisplayright.addWidget(self.liveapwidget)

        self.livemlwidget = ApMl(self.livetab)
        self.livemlwidget.setObjectName(u"livemlwidget")
        sizePolicy.setHeightForWidth(self.livemlwidget.sizePolicy().hasHeightForWidth())
        self.livemlwidget.setSizePolicy(sizePolicy)
        self.livemlwidget.setMinimumSize(QSize(400, 160))
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

        self.line_3 = QFrame(self.analysistab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.analysistoolbar.addWidget(self.line_3)

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

        self.line_4 = QFrame(self.analysistab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.analysistoolbar.addWidget(self.line_4)

        self.contribute = QCheckBox(self.analysistab)
        self.contribute.setObjectName(u"contribute")
        self.contribute.setLayoutDirection(Qt.RightToLeft)
        self.contribute.setChecked(True)
        self.contribute.setTristate(False)

        self.analysistoolbar.addWidget(self.contribute)

        self.saverecording = QPushButton(self.analysistab)
        self.saverecording.setObjectName(u"saverecording")

        self.analysistoolbar.addWidget(self.saverecording)


        self.verticalLayout_2.addLayout(self.analysistoolbar)

        self.analysisscrollarea = QScrollArea(self.analysistab)
        self.analysisscrollarea.setObjectName(u"analysisscrollarea")
        sizePolicy1.setHeightForWidth(self.analysisscrollarea.sizePolicy().hasHeightForWidth())
        self.analysisscrollarea.setSizePolicy(sizePolicy1)
        self.analysisscrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.analysisscrollarea.setWidgetResizable(True)
        self.analysiswidgetarea = QWidget()
        self.analysiswidgetarea.setObjectName(u"analysiswidgetarea")
        self.analysiswidgetarea.setGeometry(QRect(0, 0, 1208, 801))
        self.verticalLayout_3 = QVBoxLayout(self.analysiswidgetarea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget_2 = QWidget(self.analysiswidgetarea)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 400))
        self.widget_2.setStyleSheet(u"border-color: rgb(0, 0, 0);\n"
"border-thickness: 1px;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.analysisstabilogramwidget = Stabilogram(self.widget_2)
        self.analysisstabilogramwidget.setObjectName(u"analysisstabilogramwidget")
        sizePolicy1.setHeightForWidth(self.analysisstabilogramwidget.sizePolicy().hasHeightForWidth())
        self.analysisstabilogramwidget.setSizePolicy(sizePolicy1)
        self.analysisstabilogramwidget.setMinimumSize(QSize(400, 400))

        self.verticalLayout_4.addWidget(self.analysisstabilogramwidget)

        self.generalvariables = QTableWidget(self.widget_2)
        self.generalvariables.setObjectName(u"generalvariables")
        sizePolicy5.setHeightForWidth(self.generalvariables.sizePolicy().hasHeightForWidth())
        self.generalvariables.setSizePolicy(sizePolicy5)
        self.generalvariables.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.generalvariables.horizontalHeader().setStretchLastSection(True)
        self.generalvariables.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_4.addWidget(self.generalvariables)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_2.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.stancelabel_2 = QLabel(self.widget_2)
        self.stancelabel_2.setObjectName(u"stancelabel_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.stancelabel_2)

        self.stanceselect_2 = QComboBox(self.widget_2)
        self.stanceselect_2.addItem("")
        self.stanceselect_2.addItem("")
        self.stanceselect_2.addItem("")
        self.stanceselect_2.addItem("")
        self.stanceselect_2.addItem("")
        self.stanceselect_2.setObjectName(u"stanceselect_2")
        self.stanceselect_2.setEnabled(True)
        self.stanceselect_2.setEditable(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.stanceselect_2)

        self.eyelabel_2 = QLabel(self.widget_2)
        self.eyelabel_2.setObjectName(u"eyelabel_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.eyelabel_2)

        self.eyeselect_2 = QComboBox(self.widget_2)
        self.eyeselect_2.addItem("")
        self.eyeselect_2.addItem("")
        self.eyeselect_2.addItem("")
        self.eyeselect_2.setObjectName(u"eyeselect_2")
        self.eyeselect_2.setEnabled(True)
        self.eyeselect_2.setEditable(True)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.eyeselect_2)

        self.line_2 = QFrame(self.widget_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.line_2)

        self.patientinfolabel_2 = QLabel(self.widget_2)
        self.patientinfolabel_2.setObjectName(u"patientinfolabel_2")
        self.patientinfolabel_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.patientinfolabel_2)

        self.agelabel_2 = QLabel(self.widget_2)
        self.agelabel_2.setObjectName(u"agelabel_2")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.agelabel_2)

        self.ageselect_2 = QSpinBox(self.widget_2)
        self.ageselect_2.setObjectName(u"ageselect_2")
        self.ageselect_2.setEnabled(True)
        self.ageselect_2.setMaximum(130)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.ageselect_2)

        self.heightlabel_2 = QLabel(self.widget_2)
        self.heightlabel_2.setObjectName(u"heightlabel_2")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.heightlabel_2)

        self.heightselect_2 = QSpinBox(self.widget_2)
        self.heightselect_2.setObjectName(u"heightselect_2")
        self.heightselect_2.setEnabled(True)
        self.heightselect_2.setMaximum(260)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.heightselect_2)

        self.weightlabel_2 = QLabel(self.widget_2)
        self.weightlabel_2.setObjectName(u"weightlabel_2")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.weightlabel_2)

        self.weightselect_2 = QSpinBox(self.widget_2)
        self.weightselect_2.setObjectName(u"weightselect_2")
        self.weightselect_2.setEnabled(True)
        self.weightselect_2.setMaximum(1000)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.weightselect_2)

        self.commentlabel_2 = QLabel(self.widget_2)
        self.commentlabel_2.setObjectName(u"commentlabel_2")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.commentlabel_2)

        self.notesedit_2 = QPlainTextEdit(self.widget_2)
        self.notesedit_2.setObjectName(u"notesedit_2")
        self.notesedit_2.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.notesedit_2.sizePolicy().hasHeightForWidth())
        self.notesedit_2.setSizePolicy(sizePolicy6)
        self.notesedit_2.setMinimumSize(QSize(100, 30))
        self.notesedit_2.setMaximumSize(QSize(16777215, 100))

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.notesedit_2)

        self.conditionlabel_2 = QLabel(self.widget_2)
        self.conditionlabel_2.setObjectName(u"conditionlabel_2")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.conditionlabel_2)

        self.conditionselect_2 = QComboBox(self.widget_2)
        self.conditionselect_2.addItem("")
        self.conditionselect_2.addItem("")
        self.conditionselect_2.addItem("")
        self.conditionselect_2.addItem("")
        self.conditionselect_2.setObjectName(u"conditionselect_2")
        self.conditionselect_2.setEnabled(True)
        self.conditionselect_2.setEditable(True)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.conditionselect_2)

        self.testinfolabel_2 = QLabel(self.widget_2)
        self.testinfolabel_2.setObjectName(u"testinfolabel_2")
        self.testinfolabel_2.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.testinfolabel_2)

        self.medicationlabel_2 = QLabel(self.widget_2)
        self.medicationlabel_2.setObjectName(u"medicationlabel_2")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.medicationlabel_2)

        self.medicationselect_2 = QComboBox(self.widget_2)
        self.medicationselect_2.addItem("")
        self.medicationselect_2.addItem("")
        self.medicationselect_2.setObjectName(u"medicationselect_2")
        self.medicationselect_2.setEnabled(True)
        self.medicationselect_2.setEditable(True)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.medicationselect_2)

        self.identifierlabel_2 = QLabel(self.widget_2)
        self.identifierlabel_2.setObjectName(u"identifierlabel_2")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.identifierlabel_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.identifierselect_2 = QLineEdit(self.widget_2)
        self.identifierselect_2.setObjectName(u"identifierselect_2")

        self.horizontalLayout_6.addWidget(self.identifierselect_2)

        self.identifierreload_2 = QPushButton(self.widget_2)
        self.identifierreload_2.setObjectName(u"identifierreload_2")
        self.identifierreload_2.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_6.addWidget(self.identifierreload_2)


        self.formLayout_2.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_6)

        self.fallhistorylabel_2 = QLabel(self.widget_2)
        self.fallhistorylabel_2.setObjectName(u"fallhistorylabel_2")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.fallhistorylabel_2)

        self.fallhistoryselect_2 = QComboBox(self.widget_2)
        self.fallhistoryselect_2.addItem("")
        self.fallhistoryselect_2.addItem("")
        self.fallhistoryselect_2.setObjectName(u"fallhistoryselect_2")
        self.fallhistoryselect_2.setEditable(True)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.fallhistoryselect_2)


        self.verticalLayout_6.addLayout(self.formLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.apvariables = QTableWidget(self.widget_2)
        self.apvariables.setObjectName(u"apvariables")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.apvariables.sizePolicy().hasHeightForWidth())
        self.apvariables.setSizePolicy(sizePolicy7)
        self.apvariables.setMinimumSize(QSize(350, 0))
        self.apvariables.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.apvariables.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.apvariables.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_7.addWidget(self.apvariables)


        self.gridLayout.addLayout(self.verticalLayout_7, 0, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.mlvariables = QTableWidget(self.widget_2)
        self.mlvariables.setObjectName(u"mlvariables")
        sizePolicy7.setHeightForWidth(self.mlvariables.sizePolicy().hasHeightForWidth())
        self.mlvariables.setSizePolicy(sizePolicy7)
        self.mlvariables.setMinimumSize(QSize(350, 0))
        self.mlvariables.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mlvariables.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.verticalLayout_8.addWidget(self.mlvariables)


        self.gridLayout.addLayout(self.verticalLayout_8, 1, 1, 1, 1)

        self.analysismlwidget = ApMl(self.widget_2)
        self.analysismlwidget.setObjectName(u"analysismlwidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.analysismlwidget.sizePolicy().hasHeightForWidth())
        self.analysismlwidget.setSizePolicy(sizePolicy8)
        self.analysismlwidget.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.analysismlwidget, 1, 0, 1, 1)

        self.analysisapwidget = ApMl(self.widget_2)
        self.analysisapwidget.setObjectName(u"analysisapwidget")
        sizePolicy8.setHeightForWidth(self.analysisapwidget.sizePolicy().hasHeightForWidth())
        self.analysisapwidget.setSizePolicy(sizePolicy8)
        self.analysisapwidget.setMinimumSize(QSize(200, 200))

        self.gridLayout.addWidget(self.analysisapwidget, 0, 0, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)


        self.horizontalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.analysisscrollarea.setWidget(self.analysiswidgetarea)

        self.verticalLayout_2.addWidget(self.analysisscrollarea)

        self.verticalLayout_2.setStretch(1, 1)
        self.modes.addTab(self.analysistab, "")

        self.verticalLayout.addWidget(self.modes)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.modes.setCurrentIndex(0)
        self.stanceselect.setCurrentIndex(0)
        self.stanceselect_2.setCurrentIndex(0)


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
        self.stanceselect.setItemText(0, "")
        self.stanceselect.setItemText(1, QCoreApplication.translate("MainWindow", u"double legged", None))
        self.stanceselect.setItemText(2, QCoreApplication.translate("MainWindow", u"left leg", None))
        self.stanceselect.setItemText(3, QCoreApplication.translate("MainWindow", u"right leg", None))
        self.stanceselect.setItemText(4, QCoreApplication.translate("MainWindow", u"tandem", None))

        self.stanceselect.setCurrentText("")
        self.eyelabel.setText(QCoreApplication.translate("MainWindow", u"Eyes", None))
        self.eyeselect.setItemText(0, "")
        self.eyeselect.setItemText(1, QCoreApplication.translate("MainWindow", u"open", None))
        self.eyeselect.setItemText(2, QCoreApplication.translate("MainWindow", u"closed", None))

        self.eyeselect.setCurrentText("")
        self.patientinfolabel.setText(QCoreApplication.translate("MainWindow", u"Patient info", None))
        self.agelabel.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.heightlabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.heightselect.setSuffix(QCoreApplication.translate("MainWindow", u" (cm)", None))
        self.weightlabel.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.weightselect.setSuffix(QCoreApplication.translate("MainWindow", u" (Kg)", None))
        self.commentlabel.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.conditionlabel.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.conditionselect.setItemText(0, "")
        self.conditionselect.setItemText(1, QCoreApplication.translate("MainWindow", u"Healthy", None))
        self.conditionselect.setItemText(2, QCoreApplication.translate("MainWindow", u"Parkinsons", None))
        self.conditionselect.setItemText(3, QCoreApplication.translate("MainWindow", u"Stroke", None))

        self.testinfolabel.setText(QCoreApplication.translate("MainWindow", u"Test info", None))
        self.medicationlabel.setText(QCoreApplication.translate("MainWindow", u"Medication", None))
        self.medicationselect.setItemText(0, "")
        self.medicationselect.setItemText(1, QCoreApplication.translate("MainWindow", u"painkillers", None))

        self.fallhistorylabel.setText(QCoreApplication.translate("MainWindow", u"Fall history", None))
        self.fallhistoryselect.setItemText(0, "")
        self.fallhistoryselect.setItemText(1, QCoreApplication.translate("MainWindow", u"No recent incidents", None))
        self.fallhistoryselect.setItemText(2, QCoreApplication.translate("MainWindow", u"Fell in last year", None))

        self.identifierlabel.setText(QCoreApplication.translate("MainWindow", u"Identifier", None))
        self.identifierreload.setText(QCoreApplication.translate("MainWindow", u"regenerate", None))
        self.modes.setTabText(self.modes.indexOf(self.livetab), QCoreApplication.translate("MainWindow", u"Live", None))
        self.analysisopenfile.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.analysisplay.setText(QCoreApplication.translate("MainWindow", u"\u23ef\ufe0f", None))
        self.currenttime.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.maxtime.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.analysisrestart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.contribute.setText(QCoreApplication.translate("MainWindow", u"Contribute to reseach?", None))
        self.saverecording.setText(QCoreApplication.translate("MainWindow", u"Save report", None))
        self.stancelabel_2.setText(QCoreApplication.translate("MainWindow", u"Stance", None))
        self.stanceselect_2.setItemText(0, "")
        self.stanceselect_2.setItemText(1, QCoreApplication.translate("MainWindow", u"double legged", None))
        self.stanceselect_2.setItemText(2, QCoreApplication.translate("MainWindow", u"left leg", None))
        self.stanceselect_2.setItemText(3, QCoreApplication.translate("MainWindow", u"right leg", None))
        self.stanceselect_2.setItemText(4, QCoreApplication.translate("MainWindow", u"tandem", None))

        self.stanceselect_2.setCurrentText("")
        self.eyelabel_2.setText(QCoreApplication.translate("MainWindow", u"Eyes", None))
        self.eyeselect_2.setItemText(0, "")
        self.eyeselect_2.setItemText(1, QCoreApplication.translate("MainWindow", u"open", None))
        self.eyeselect_2.setItemText(2, QCoreApplication.translate("MainWindow", u"closed", None))

        self.eyeselect_2.setCurrentText("")
        self.patientinfolabel_2.setText(QCoreApplication.translate("MainWindow", u"Patient info", None))
        self.agelabel_2.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.heightlabel_2.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.heightselect_2.setSuffix(QCoreApplication.translate("MainWindow", u" (cm)", None))
        self.weightlabel_2.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.weightselect_2.setSuffix(QCoreApplication.translate("MainWindow", u" (Kg)", None))
        self.commentlabel_2.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
        self.conditionlabel_2.setText(QCoreApplication.translate("MainWindow", u"Condition", None))
        self.conditionselect_2.setItemText(0, "")
        self.conditionselect_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Healthy", None))
        self.conditionselect_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Parkinsons", None))
        self.conditionselect_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Stroke", None))

        self.testinfolabel_2.setText(QCoreApplication.translate("MainWindow", u"Test info | <DATE> | <TIME>", None))
        self.medicationlabel_2.setText(QCoreApplication.translate("MainWindow", u"Medication", None))
        self.medicationselect_2.setItemText(0, "")
        self.medicationselect_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Painkillers", None))

        self.identifierlabel_2.setText(QCoreApplication.translate("MainWindow", u"Identifier", None))
        self.identifierreload_2.setText(QCoreApplication.translate("MainWindow", u"regemerate", None))
        self.fallhistorylabel_2.setText(QCoreApplication.translate("MainWindow", u"Fall history", None))
        self.fallhistoryselect_2.setItemText(0, QCoreApplication.translate("MainWindow", u"No recent incidents", None))
        self.fallhistoryselect_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Fell in last year", None))

        self.modes.setTabText(self.modes.indexOf(self.analysistab), QCoreApplication.translate("MainWindow", u"Analysis", None))
    # retranslateUi

