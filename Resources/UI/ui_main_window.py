# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windoweqSKMd.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QToolBar, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1120, 720)
        MainWindow.setMinimumSize(QSize(1120, 720))
        MainWindow.setStyleSheet(u"/* Central Widget */\n"
"QWidget#centralwidget {\n"
"    background-color: #1e1e1e;  /* Dark gray background */\n"
"    border: none;               /* No border for a cleaner look */\n"
"    padding: 15px;              /* Padding inside the central widget */\n"
"}\n"
"\n"
"/* QMenuBar */\n"
"QMenuBar {\n"
"    background-color: #2e2e2e;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text */\n"
"    border-bottom: 1px solid #5b5e60;  /* Light gray border for separation */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: transparent; /* Transparent background */\n"
"    padding: 6px 12px;             /* Padding for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"}\n"
"\n"
"QMenuBar::item:selected {          /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenuBar::item:pressed {           /* Pressed menu item */\n"
"    bac"
                        "kground-color: #3d78b2;     /* Darker blue on press */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"/* QMenu */\n"
"QMenu {\n"
"    background-color: #2e2e2e;     /* Dark gray background for menus */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"    padding: 6px;                  /* Padding inside the menu */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background-color: transparent; /* Transparent background for menu items */\n"
"    color: #ffffff;                /* White text */\n"
"    padding: 6px 12px;             /* Padding for each menu item */\n"
"}\n"
"\n"
"QMenu::item:selected {             /* Hovered menu item */\n"
"    background-color: #4a90e2;     /* Light blue background on hover */\n"
"    color: #ffffff;                /* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::item:pressed {              /* Pressed menu item */\n"
"    background-color: #3d78b2;     /* Darker blue background on press */\n"
"    color: #ffffff;                /"
                        "* Ensure text remains white */\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background-color: #5b5e60;     /* Light gray separator between items */\n"
"    margin: 6px 0;                 /* Spacing around the separator */\n"
"}\n"
"\n"
"/* QMenu::indicator (checkboxes and radio buttons in menus) */\n"
"QMenu::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    background-color: #2e2e2e;     /* Dark gray background for indicators */\n"
"    border: 1px solid #5b5e60;     /* Light gray border */\n"
"    border-radius: 2px;            /* Slightly rounded corners */\n"
"}\n"
"\n"
"QMenu::indicator:checked {\n"
"    background-color: #4a90e2;     /* Light blue when checked */\n"
"    border-color: #3d78b2;         /* Darker blue border when checked */\n"
"}\n"
"\n"
"QMenu::indicator:unchecked {\n"
"    background-color: #2e2e2e;     /* Keep the dark gray when unchecked */\n"
"    border-color: #5b5e60;         /* Light gray border when unchecked */\n"
"}\n"
"\n"
"/* Submenus */\n"
"QMen"
                        "u::right-arrow {\n"
"    image: url(':/icons/right-arrow.png'); /* Replace with an appropriate icon path */\n"
"    padding: 0px 10px;                     /* Space before submenu arrows */\n"
"}\n"
"\n"
"/* QToolBar */\n"
"QToolBar {\n"
"    background-color: #2e2e2e;      /* Dark gray background */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    padding: 4px;                   /* Padding inside the toolbar */\n"
"    spacing: 4px;                   /* Spacing between toolbar buttons */\n"
"}\n"
"\n"
"QToolBar::handle {\n"
"    background-color: #5b5e60;      /* Light gray handle for draggable toolbars */\n"
"    width: 10px;                    /* Width of the handle */\n"
"    margin: 4px;                    /* Margin around the handle */\n"
"}\n"
"\n"
"QToolBar::separator {\n"
"    background-color: #5b5e60;      /* Light gray for separators */\n"
"    width: 1px;                     /* Thickness of the separator */\n"
"    height: 24px;                   /* Height of the separator */"
                        "\n"
"    margin: 6px;                    /* Space around the separator */\n"
"}\n"
"\n"
"QToolBar::item {\n"
"    padding: 4px;                   /* Padding for individual toolbar items */\n"
"}\n"
"\n"
"/* QToolButton in Toolbar */\n"
"QToolButton {\n"
"    background-color: #3c3f41;      /* Dark gray background for toolbar buttons */\n"
"    color: #ffffff;                 /* White text/icon */\n"
"    border: 1px solid #5b5e60;      /* Light gray border */\n"
"    border-radius: 4px;             /* Rounded corners */\n"
"    padding: 6px 12px;              /* Padding for comfortable button size */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4a90e2;      /* Light blue on hover */\n"
"    border-color: #3d78b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
"    border-color: #2a5f92;          /* Even darker border when pressed */\n"
"}\n"
"\n"
"QToolButton:checked {\n"
"    background-colo"
                        "r: #3d78b2;      /* Darker blue when checked */\n"
"    border-color: #2a5f92;          /* Border color when checked */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #2e2e2e;      /* Dark gray when disabled */\n"
"    color: #777777;                 /* Lighter gray text/icon for disabled state */\n"
"    border-color: #5b5e60;          /* Keep the border color same as normal state */\n"
"}\n"
"\n"
"/* QToolButton::menu-button */\n"
"QToolButton::menu-button {\n"
"    background-color: #3c3f41;      /* Dark gray background for menu button */\n"
"    border: 1px solid #5b5e60;      /* Light gray border for menu button */\n"
"    padding: 4px;                   /* Padding for the menu button */\n"
"}\n"
"\n"
"QToolButton::menu-button:hover {\n"
"    background-color: #4a90e2;      /* Light blue on hover */\n"
"    border-color: #3d78b2;          /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton::menu-button:pressed {\n"
"    background-color: #3d78b2;      /* Darker blue on press */\n"
""
                        "    border-color: #2a5f92;          /* Even darker border on press */\n"
"}\n"
"\n"
"/* QStatusBar */\n"
"QStatusBar {\n"
"    background-color: #2e2e2e;   /* Dark gray background */\n"
"    border-top: 1px solid #5b5e60; /* Light gray top border for separation */\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 13px;             /* Slightly smaller font for the status bar */\n"
"    padding: 6px;                /* Padding inside the status bar */\n"
"}\n"
"\n"
"QStatusBar::item {\n"
"    border: none;                /* No border around individual status items */\n"
"    padding: 0px 5px;            /* Padding between status bar items */\n"
"}\n"
"\n"
"QStatusBar QLabel {\n"
"    color: #ffffff;              /* White text for any QLabel inside the status bar */\n"
"    background-color: transparent; /* Ensure QLabel in status bar matches the bar's background */\n"
"}\n"
"\n"
"QStatusBar::indicator {\n"
"    background-color: #4a90e2;   /* Optional indicator styling, e.g., for icons or s"
                        "tatus signals */\n"
"    border-radius: 4px;          /* Rounded corners for any indicator elements */\n"
"}\n"
"\n"
"/* Scroll Area Styling (optional) */\n"
"QScrollArea {\n"
"    background-color: transparent; /* Transparent to match the central widget */\n"
"    border: none;                  /* No border */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: #3c3f41;    /* Darker gray for scroll bar background */\n"
"    width: 12px;                  /* Scroll bar width */\n"
"    margin: 22px 0 22px 0;        /* Top and bottom margins */\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #5b5e60;    /* Slightly lighter gray for scroll handle */\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: none;             /* Remove arrows */\n"
"}\n"
"\n"
"/* QPushButton */\n"
"QPushButton {\n"
"    background-color: #3c3f41;  /* Dark gray background */\n"
"    color: #ffffff;             /* White text */\n"
"   "
                        " border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"	padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4a90e2;  /* Light blue on hover */\n"
"    border-color: #3d78b2;      /* Darker blue border */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;  /* Darker blue on press */\n"
"    border-color: #2a5f92;      /* Even darker border when pressed */\n"
"}\n"
"\n"
"/* QLabel */\n"
"QLabel {\n"
"    color: #ffffff;             /* White text */\n"
"    font-size: 14px;            /* Set font size */\n"
"}\n"
"\n"
"/* QFrame */\n"
"QFrame {\n"
"    background-color: #2e2e2e;  /* Dark gray for frames */\n"
"}\n"
"\n"
"/* QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #2e2e2e;  /* Dark gray background for input fields */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 4px;         /* Rounded corners */\n"
"}\n"
""
                        "\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border when focused */\n"
"    background-color: #333333;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #2b2b2b;  /* Darker gray background for text area */\n"
"    color: #ffffff;             /* White text */\n"
"    border: 1px solid #5b5e60;  /* Light gray border */\n"
"    border-radius: 0px;         /* No rounded corners */\n"
"    padding: 10px;              /* Comfortable padding for text input */\n"
"    font-size: 13px;            /* Slightly smaller font */\n"
"    line-height: 1.4;           /* Adjust line spacing for readability */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    border-color: #4a90e2;      /* Light blue border on focus */\n"
"    background-color: #3a3a3a;  /* Slightly lighter gray on focus */\n"
"}\n"
"\n"
"/* QRadioButton */\n"
"QRadioButton {\n"
"    color: #ffffff;              /* White text */\n"
"    font-size: 14px;             /* "
                        "Font size for readability */\n"
"    spacing: 5px;                /* Space between radio button and label */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;                 /* Size of the radio button */\n"
"    height: 16px;\n"
"    background-color: #2e2e2e;   /* Dark gray background for the indicator */\n"
"    border: 1px solid #5b5e60;   /* Light gray border */\n"
"    border-radius: 8px;          /* Circular radio button */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;   /* Light blue on hover */\n"
"    border-color: #3d78b2;       /* Darker blue border on hover */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;   /* Light blue when checked */\n"
"    border-color: #3d78b2;       /* Darker blue border when checked */\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue on press */\n"
"    border-color: #2a5f92;       /* Even darker border on press */\n"
"}\n"
"\n"
"QRadio"
                        "Button::indicator:checked:pressed {\n"
"    background-color: #3d78b2;   /* Darker blue when checked and pressed */\n"
"    border-color: #2a5f92;       /* Even darker border when checked and pressed */\n"
"}\n"
"\n"
"/* QToolButton */\n"
"QToolButton {\n"
"    background-color: #3c3f41;    /* Dark gray background */\n"
"    color: #ffffff;               /* White text/icon */\n"
"    border: 1px solid #5b5e60;    /* Light gray border */\n"
"    border-radius: 4px;           /* Rounded corners */\n"
"    padding: 6px 12px;            /* Padding for comfortable button size */\n"
"    font-size: 14px;              /* Font size for text (if any) */\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #4a90e2;    /* Light blue background on hover */\n"
"    border-color: #3d78b2;        /* Darker blue border on hover */\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"    background-color: #3d78b2;    /* Darker blue background on press */\n"
"    border-color: #2a5f92;        /* Even darker border when pressed */\n"
""
                        "}\n"
"\n"
"QToolButton:checked {\n"
"    background-color: #3d78b2;    /* Darker blue when checked */\n"
"    border-color: #2a5f92;        /* Border color when checked */\n"
"}\n"
"\n"
"QToolButton:disabled {\n"
"    background-color: #2e2e2e;    /* Dark gray when disabled */\n"
"    color: #777777;               /* Lighter gray text/icon for disabled state */\n"
"    border-color: #5b5e60;        /* Keep the border color same as normal state */\n"
"}\n"
"")
        self.actionAbout_asset_manager = QAction(MainWindow)
        self.actionAbout_asset_manager.setObjectName(u"actionAbout_asset_manager")
        self.actionCurrent_Asset_Only = QAction(MainWindow)
        self.actionCurrent_Asset_Only.setObjectName(u"actionCurrent_Asset_Only")
        self.actionAll_Assets = QAction(MainWindow)
        self.actionAll_Assets.setObjectName(u"actionAll_Assets")
        self.actionToolbar = QAction(MainWindow)
        self.actionToolbar.setObjectName(u"actionToolbar")
        self.actionToolbar.setCheckable(True)
        self.actionStatus_Bar = QAction(MainWindow)
        self.actionStatus_Bar.setObjectName(u"actionStatus_Bar")
        self.actionStatus_Bar.setCheckable(True)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionAssociate_File_Types = QAction(MainWindow)
        self.actionAssociate_File_Types.setObjectName(u"actionAssociate_File_Types")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"QFrame {margin-left: 6px; margin-right: 6px; margin-bottom: 6px;}")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {margin: 0px;}")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_7)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_7)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_8)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_9)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_9)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_9)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_10)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_10)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setFont(font)

        self.horizontalLayout_4.addWidget(self.pushButton_7)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)

        self.verticalLayout_3.addWidget(self.frame_10)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.listWidget = QListWidget(self.frame_5)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_5.addWidget(self.listWidget)

        self.listWidget_2 = QListWidget(self.frame_5)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_5.addWidget(self.listWidget_2)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout.addWidget(self.frame)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(Qt.ToolBarArea.AllToolBarAreas)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1120, 29))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuPC_Convert = QMenu(self.menuBar)
        self.menuPC_Convert.setObjectName(u"menuPC_Convert")
        self.menuHelp = QMenu(self.menuBar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuPC_Convert.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionAssociate_File_Types)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionToolbar)
        self.menuView.addAction(self.actionStatus_Bar)
        self.menuPC_Convert.addAction(self.actionCurrent_Asset_Only)
        self.menuPC_Convert.addSeparator()
        self.menuPC_Convert.addAction(self.actionAll_Assets)
        self.menuHelp.addAction(self.actionAbout_asset_manager)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phils-Hub - Drag N Drop Asset Manager", None))
        self.actionAbout_asset_manager.setText(QCoreApplication.translate("MainWindow", u"About asset_manager...", None))
        self.actionCurrent_Asset_Only.setText(QCoreApplication.translate("MainWindow", u"Current Asset Only", None))
#if QT_CONFIG(shortcut)
        self.actionCurrent_Asset_Only.setShortcut(QCoreApplication.translate("MainWindow", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.actionAll_Assets.setText(QCoreApplication.translate("MainWindow", u"All Assets", None))
#if QT_CONFIG(shortcut)
        self.actionAll_Assets.setShortcut(QCoreApplication.translate("MainWindow", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.actionToolbar.setText(QCoreApplication.translate("MainWindow", u"Toolbar", None))
        self.actionStatus_Bar.setText(QCoreApplication.translate("MainWindow", u"Status Bar", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New...", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As...", None))
        self.actionAssociate_File_Types.setText(QCoreApplication.translate("MainWindow", u"Associate File Types...", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"New Entry", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete Entry", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Find Entry", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Copy to", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Rename Entry", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Copy Entry", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Paste from", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuPC_Convert.setTitle(QCoreApplication.translate("MainWindow", u"PC Convert", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

