# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maingui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class QLineEdit(QtWidgets.QLineEdit):
    focus_in_signal = QtCore.pyqtSignal()
    focus_out_signal = QtCore.pyqtSignal()
    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.FocusIn:
            return 1
    def focusInEvent(self, event):
        self.focus_in_signal.emit()
        super().focusInEvent(event)

    def focusOutEvent(self, event):
        super().focusOutEvent(event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1180, 770)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(255,255,255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.main)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame = QtWidgets.QFrame(self.main)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tab_alt = QtWidgets.QTabWidget(self.frame)
        self.tab_alt.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setPointSize(17)
        self.tab_alt.setFont(font)
        self.tab_alt.setTabletTracking(True)
        self.tab_alt.setAcceptDrops(False)
        self.tab_alt.setAutoFillBackground(False)
        self.tab_alt.setStyleSheet("QWidget { background-color:#AED6F1; }")
        self.tab_alt.setTabPosition(QtWidgets.QTabWidget.South)
        self.tab_alt.setElideMode(QtCore.Qt.ElideRight)
        self.tab_alt.setDocumentMode(False)
        self.tab_alt.setMovable(False)
        self.tab_alt.setTabBarAutoHide(False)
        self.tab_alt.setObjectName("tab_alt")
        self.map = QtWidgets.QWidget()
        self.map.setObjectName("map")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.map)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.refresh = QtWidgets.QPushButton(self.map)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.refresh.setFont(font)
        self.refresh.setTabletTracking(True)
        self.refresh.setStyleSheet("QWidget { background-color:rgb(212, 212, 212); }")
        self.refresh.setAutoDefault(True)
        self.refresh.setDefault(False)
        self.refresh.setFlat(False)
        self.refresh.setObjectName("refresh")
        self.gridLayout_14.addWidget(self.refresh, 1, 0, 1, 1)
        self.send_image = QtWidgets.QPushButton(self.map)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_image.sizePolicy().hasHeightForWidth())
        self.send_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.send_image.setFont(font)
        self.send_image.setTabletTracking(True)
        self.send_image.setStyleSheet("QWidget { background-color:rgb(212, 212, 212); }")
        self.send_image.setAutoDefault(False)
        self.send_image.setDefault(False)
        self.send_image.setFlat(False)
        self.send_image.setObjectName("send_image")
        self.gridLayout_14.addWidget(self.send_image, 1, 1, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.map)
        self.graphicsView.setTabletTracking(True)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_14.addWidget(self.graphicsView, 0, 0, 1, 2)
        self.tab_alt.addTab(self.map, "")
        self.information = QtWidgets.QWidget()
        self.information.setObjectName("information")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.information)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.information)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tab_alt.addTab(self.information, "")
        self.usage = QtWidgets.QWidget()
        self.usage.setObjectName("usage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.usage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.guide = QtWidgets.QTextEdit(self.usage)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.guide.setFont(font)
        self.guide.setStyleSheet("\n"
"font: 18pt \"Arial\";")
        self.guide.setReadOnly(True)
        self.guide.setObjectName("guide")
        self.verticalLayout_2.addWidget(self.guide)
        self.tab_alt.addTab(self.usage, "")
        self.gridLayout_3.addWidget(self.tab_alt, 1, 0, 1, 2)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.click_to_search = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.click_to_search.setFont(font)
        self.click_to_search.setTabletTracking(True)
        self.click_to_search.setStyleSheet("background-color:rgb(202, 202, 202)")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/lookup-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.click_to_search.setIcon(icon)
        self.click_to_search.setIconSize(QtCore.QSize(50, 50))
        self.click_to_search.setObjectName("click_to_search")
        self.gridLayout_2.addWidget(self.click_to_search, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(618, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.logo = QtWidgets.QLabel(self.frame_5)
        self.logo.setMaximumSize(QtCore.QSize(80, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/map/iconguider.ico"))
        self.logo.setScaledContents(True)
        self.logo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.logo.setObjectName("logo")
        self.gridLayout_2.addWidget(self.logo, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame_5, 0, 1, 1, 1)
        self.frame_ = QtWidgets.QFrame(self.frame)
        self.frame_.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_.setObjectName("frame_")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.frame_)
        self.label.setMaximumSize(QtCore.QSize(200, 110))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget { color:rgb(46, 102, 255);background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69)) }")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(7)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("icon/guider.png"))
        self.label.setScaledContents(True)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.main)
        self.search_bar = QtWidgets.QWidget()
        self.search_bar.setObjectName("search_bar")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.search_bar)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_3 = QtWidgets.QFrame(self.search_bar)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem1 = QtWidgets.QSpacerItem(981, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.room_building = QtWidgets.QTableView(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.room_building.setFont(font)
        self.room_building.setTabletTracking(True)
        self.room_building.setStyleSheet("mvkldv\n"
"klsaklsa")
        self.room_building.setObjectName("room_building")
        self.gridLayout_7.addWidget(self.room_building, 2, 0, 1, 5)
        self.departure = QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.departure.setFont(font)
        self.departure.setTabletTracking(True)
        self.departure.setInputMask("")
        self.departure.setFrame(True)
        self.departure.setEchoMode(QLineEdit.Normal)
        self.departure.setCursorPosition(2)
        self.departure.setReadOnly(False)
        self.departure.setClearButtonEnabled(True)
        self.departure.setObjectName("departure")
        self.gridLayout_7.addWidget(self.departure, 1, 0, 1, 1)
        self.start_lookup = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_lookup.setFont(font)
        self.start_lookup.setTabletTracking(True)
        self.start_lookup.setStyleSheet("background-color:rgb(255, 251, 224)")
        self.start_lookup.setIcon(icon)
        self.start_lookup.setIconSize(QtCore.QSize(50, 50))
        self.start_lookup.setObjectName("start_lookup")
        self.gridLayout_7.addWidget(self.start_lookup, 0, 2, 2, 1)
        self.destination = QLineEdit(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.destination.setFont(font)
        self.destination.setTabletTracking(True)
        self.destination.setInputMask("")
        self.destination.setText("")
        self.destination.setFrame(True)
        self.destination.setEchoMode(QLineEdit.Normal)
        self.destination.setCursorPosition(0)
        self.destination.setReadOnly(False)
        self.destination.setClearButtonEnabled(True)
        self.destination.setObjectName("destination")
        self.gridLayout_7.addWidget(self.destination, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(677, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 4, 2, 1)
        self.start_lookup_2 = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_lookup_2.setFont(font)
        self.start_lookup_2.setTabletTracking(True)
        self.start_lookup_2.setStyleSheet("background-color:rgb(255, 251, 224)")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/map/search-information-pngrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.start_lookup_2.setIcon(icon1)
        self.start_lookup_2.setIconSize(QtCore.QSize(50, 50))
        self.start_lookup_2.setObjectName("start_lookup_2")
        self.gridLayout_7.addWidget(self.start_lookup_2, 0, 3, 2, 1)
        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 2)
        self.backbutton1 = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.backbutton1.setFont(font)
        self.backbutton1.setTabletTracking(True)
        self.backbutton1.setStyleSheet("background-color:rgb(255, 251, 224)")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/back-icon-png-17.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backbutton1.setIcon(icon2)
        self.backbutton1.setIconSize(QtCore.QSize(30, 30))
        self.backbutton1.setObjectName("backbutton1")
        self.gridLayout.addWidget(self.backbutton1, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.search_bar)
        self.page_info = QtWidgets.QWidget()
        self.page_info.setObjectName("page_info")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_info)
        self.gridLayout_12.setObjectName("gridLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(957, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem3, 0, 1, 1, 1)
        self.backbutton2 = QtWidgets.QPushButton(self.page_info)
        self.backbutton2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.backbutton2.setFont(font)
        self.backbutton2.setTabletTracking(True)
        self.backbutton2.setStyleSheet("background-color:rgb(255, 251, 224)\n"
"")
        self.backbutton2.setIcon(icon2)
        self.backbutton2.setIconSize(QtCore.QSize(30, 30))
        self.backbutton2.setObjectName("backbutton2")
        self.gridLayout_12.addWidget(self.backbutton2, 0, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.page_info)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_11.setObjectName("gridLayout_11")
        spacerItem4 = QtWidgets.QSpacerItem(767, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem4, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(197, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem5, 2, 2, 1, 1)
        self.find_path = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.find_path.setFont(font)
        self.find_path.setTabletTracking(True)
        self.find_path.setStyleSheet("background-color:rgb(255, 251, 224)\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/map/download (1).jfif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.find_path.setIcon(icon3)
        self.find_path.setIconSize(QtCore.QSize(45, 45))
        self.find_path.setObjectName("find_path")
        self.gridLayout_11.addWidget(self.find_path, 2, 1, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.frame_7)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.info_room = QtWidgets.QTextEdit(self.frame_8)
        self.info_room.setReadOnly(True)
        self.info_room.setObjectName("info_room")
        self.gridLayout_10.addWidget(self.info_room, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.frame_8, 0, 0, 1, 1)
        self.image_room = QtWidgets.QLabel(self.frame_7)
        self.image_room.setText("")
        self.image_room.setPixmap(QtGui.QPixmap("khohtmt.jpg"))
        self.image_room.setScaledContents(True)
        self.image_room.setObjectName("image_room")
        self.gridLayout_11.addWidget(self.image_room, 0, 1, 1, 2)
        self.gridLayout_12.addWidget(self.frame_7, 1, 0, 1, 2)
        self.stackedWidget.addWidget(self.page_info)
        self.gridLayout_8.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1180, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tab_alt.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tab_alt, self.send_image)
        MainWindow.setTabOrder(self.send_image, self.refresh)
        MainWindow.setTabOrder(self.refresh, self.guide)
        MainWindow.setTabOrder(self.guide, self.click_to_search)
        MainWindow.setTabOrder(self.click_to_search, self.destination)
        MainWindow.setTabOrder(self.destination, self.departure)
        MainWindow.setTabOrder(self.departure, self.start_lookup)
        MainWindow.setTabOrder(self.start_lookup, self.room_building)
        MainWindow.setTabOrder(self.room_building, self.backbutton1)
        MainWindow.setTabOrder(self.backbutton1, self.backbutton2)
        MainWindow.setTabOrder(self.backbutton2, self.find_path)
        MainWindow.setTabOrder(self.find_path, self.info_room)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refresh.setText(_translate("MainWindow", "Làm mới"))
        self.send_image.setText(_translate("MainWindow", "Gửi hình"))
        self.tab_alt.setTabText(self.tab_alt.indexOf(self.map), _translate("MainWindow", "BẢN ĐỒ"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline;\">GIỚI THIỆU</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:17pt;\">Xin chào bạn, đây là sản phẩm đến từ nhóm sinh viên trong cuộc thi Bách Khoa Innovation. Chúng tôi hi vọng thiết bị này có thể giải quyết vấn đề tìm đường trong các khu vực lớn.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,sans-serif\'; font-size:17pt;\">Chúc bạn có những trải nghiệm thú vị với sản phẩm mới lạ này. Xin cảm ơn!</span><span style=\" font-size:8pt;\"> </span></p></body></html>"))
        self.tab_alt.setTabText(self.tab_alt.indexOf(self.information), _translate("MainWindow", "THÔNG TIN"))
        self.guide.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; text-decoration: underline;\">HƯỚNG DẪN SỬ DỤNG</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Chọn thanh tìm kiếm</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Chọn kính lúp bagts đầu tìm kiếm</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Ấn vào chỉ đường</p></body></html>"))
        self.tab_alt.setTabText(self.tab_alt.indexOf(self.usage), _translate("MainWindow", "HƯỚNG DẪN"))
        self.click_to_search.setText(_translate("MainWindow", "Bạn muốn đi đâu ?"))
        self.departure.setText(_translate("MainWindow", "B4"))
        self.departure.setPlaceholderText(_translate("MainWindow", "Điểm bắt đầu"))
        self.start_lookup.setText(_translate("MainWindow", "Tìm đường"))
        self.destination.setPlaceholderText(_translate("MainWindow", "Nhập địa điểm bạn muốn đến"))
        self.start_lookup_2.setText(_translate("MainWindow", "Thông tin\n"
"điểm đến"))
        self.backbutton1.setText(_translate("MainWindow", "Quay lại"))
        self.backbutton2.setText(_translate("MainWindow", "Quay lại"))
        self.find_path.setText(_translate("MainWindow", "Chỉ đường"))
        self.info_room.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"0\" cellpadding=\"0\" bgcolor=\"#ffffff\">\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\"><br /></span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">Văn phòng</span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">KHOA KHOA HỌC VÀ KĨ THUẬT MÁY TÍNH</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; color:#333333;\">: A3 – 268 Lý Thường Kiệt, Q. 10, TP. HCM</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">Điện thoại</span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; color:#333333;\">: (84.8) 8.647.256 - Ext: 5847</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">Fax</span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; color:#333333;\">: (84.8) 8.645.137</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">Website</span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; color:#333333;\">: </span><a href=\"http://www.cse.hcmut.edu.vn/\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; text-decoration: underline; color:#428bca; background-color:transparent;\">http://www.cse.hcmut.edu.vn</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">Email</span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; color:#333333;\">: </span><a href=\"mailto:welcome@cse.hcmut.edu.vn\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; text-decoration: underline; color:#428bca; background-color:transparent;\">welcome@cse.hcmut.edu.vn</span></a></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">Trưởng khoa</span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; color:#333333;\">: TS Phạm Trần Vũ</span></p></td></tr>\n"
"<tr>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; font-weight:600; color:#333333;\">Email của Trưởng khoa</span></p></td>\n"
"<td style=\" padding-left:0; padding-right:0; padding-top:0; padding-bottom:0;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,helvetica,sans-serif\'; font-size:18pt; color:#333333;\">: </span><a href=\"http://ptvu@cse.hcmut.edu.vn/\"><span style=\" font-family:\'verdana,geneva,sans-serif\'; font-size:18pt; text-decoration: underline; color:#428bca; background-color:transparent;\">ptvu@cse.hcmut.edu.vn</span></a></p></td></tr></table>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
import map_rc
