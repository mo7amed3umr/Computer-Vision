# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI8.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1006, 575)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.selectimg = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selectimg.setFont(font)
        self.selectimg.setObjectName("selectimg")
        self.selectimg.addItem("")
        self.selectimg.addItem("")
        self.selectimg.addItem("")
        self.gridLayout_2.addWidget(self.selectimg, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.colorimg = ImageView(self.layoutWidget)
        self.colorimg.setObjectName("colorimg")
        self.horizontalLayout_2.addWidget(self.colorimg)
        self.grayimg = ImageView(self.layoutWidget)
        self.grayimg.setObjectName("grayimg")
        self.horizontalLayout_2.addWidget(self.grayimg)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_4.addWidget(self.splitter_2)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.gridLayout = QtWidgets.QGridLayout(self.tab1)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.tab1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.noise = QtWidgets.QComboBox(self.layoutWidget2)
        self.noise.setObjectName("noise")
        self.noise.addItem("")
        self.noise.addItem("")
        self.noise.addItem("")
        self.noise.addItem("")
        self.horizontalLayout_7.addWidget(self.noise)
        self.filter = QtWidgets.QComboBox(self.layoutWidget2)
        self.filter.setObjectName("filter")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.filter.addItem("")
        self.horizontalLayout_7.addWidget(self.filter)
        self.edge = QtWidgets.QComboBox(self.layoutWidget2)
        self.edge.setObjectName("edge")
        self.edge.addItem("")
        self.edge.addItem("")
        self.edge.addItem("")
        self.edge.addItem("")
        self.edge.addItem("")
        self.horizontalLayout_7.addWidget(self.edge)
        self.layoutWidget3 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.noise_view = ImageView(self.layoutWidget3)
        self.noise_view.setObjectName("noise_view")
        self.horizontalLayout_8.addWidget(self.noise_view)
        self.filter_view = ImageView(self.layoutWidget3)
        self.filter_view.setObjectName("filter_view")
        self.horizontalLayout_8.addWidget(self.filter_view)
        self.edge_view = ImageView(self.layoutWidget3)
        self.edge_view.setObjectName("edge_view")
        self.horizontalLayout_8.addWidget(self.edge_view)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.histogram = QtWidgets.QPushButton(self.tab2)
        self.histogram.setObjectName("histogram")
        self.horizontalLayout_5.addWidget(self.histogram)
        self.curve = QtWidgets.QPushButton(self.tab2)
        self.curve.setObjectName("curve")
        self.horizontalLayout_5.addWidget(self.curve)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.histogram_view = PlotWidget(self.tab2)
        self.histogram_view.setObjectName("histogram_view")
        self.horizontalLayout_6.addWidget(self.histogram_view)
        self.curve_view = PlotWidget(self.tab2)
        self.curve_view.setObjectName("curve_view")
        self.horizontalLayout_6.addWidget(self.curve_view)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.original_img = ImageView(self.tab)
        self.original_img.setObjectName("original_img")
        self.horizontalLayout_10.addWidget(self.original_img)
        self.equalize_view = ImageView(self.tab)
        self.equalize_view.setObjectName("equalize_view")
        self.horizontalLayout_10.addWidget(self.equalize_view)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.equalize = QtWidgets.QPushButton(self.tab)
        self.equalize.setObjectName("equalize")
        self.verticalLayout_6.addWidget(self.equalize)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.Tab4 = QtWidgets.QWidget()
        self.Tab4.setObjectName("Tab4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Tab4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.normalize = QtWidgets.QPushButton(self.Tab4)
        self.normalize.setObjectName("normalize")
        self.horizontalLayout_3.addWidget(self.normalize)
        self.local_butt = QtWidgets.QPushButton(self.Tab4)
        self.local_butt.setObjectName("local_butt")
        self.horizontalLayout_3.addWidget(self.local_butt)
        self.global_butt = QtWidgets.QPushButton(self.Tab4)
        self.global_butt.setObjectName("global_butt")
        self.horizontalLayout_3.addWidget(self.global_butt)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.normalize_view = ImageView(self.Tab4)
        self.normalize_view.setObjectName("normalize_view")
        self.horizontalLayout_4.addWidget(self.normalize_view)
        self.local_view = ImageView(self.Tab4)
        self.local_view.setObjectName("local_view")
        self.horizontalLayout_4.addWidget(self.local_view)
        self.global_view = ImageView(self.Tab4)
        self.global_view.setObjectName("global_view")
        self.horizontalLayout_4.addWidget(self.global_view)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Tab4, "")
        self.tab5 = QtWidgets.QWidget()
        self.tab5.setObjectName("tab5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.hybrid_view1 = ImageView(self.tab5)
        self.hybrid_view1.setObjectName("hybrid_view1")
        self.horizontalLayout_9.addWidget(self.hybrid_view1)
        self.hybrid_view2 = ImageView(self.tab5)
        self.hybrid_view2.setObjectName("hybrid_view2")
        self.horizontalLayout_9.addWidget(self.hybrid_view2)
        self.hybrid_view3 = ImageView(self.tab5)
        self.hybrid_view3.setObjectName("hybrid_view3")
        self.horizontalLayout_9.addWidget(self.hybrid_view3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.hybrid = QtWidgets.QPushButton(self.tab5)
        self.hybrid.setObjectName("hybrid")
        self.verticalLayout.addWidget(self.hybrid)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_12.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_12.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget = ImageView(self.tab_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_11.addWidget(self.widget)
        self.widget_2 = ImageView(self.tab_2)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_11.addWidget(self.widget_2)
        self.widget_5 = ImageView(self.tab_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_11.addWidget(self.widget_5)
        self.widget_3 = ImageView(self.tab_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_11.addWidget(self.widget_3)
        self.widget_4 = ImageView(self.tab_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_11.addWidget(self.widget_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.gridLayout_6.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.histo_r = PlotWidget(self.tab_3)
        self.histo_r.setObjectName("histo_r")
        self.horizontalLayout_14.addWidget(self.histo_r)
        self.histo_g = PlotWidget(self.tab_3)
        self.histo_g.setObjectName("histo_g")
        self.horizontalLayout_14.addWidget(self.histo_g)
        self.histo_b = PlotWidget(self.tab_3)
        self.histo_b.setObjectName("histo_b")
        self.horizontalLayout_14.addWidget(self.histo_b)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.rgb = QtWidgets.QPushButton(self.tab_3)
        self.rgb.setObjectName("rgb")
        self.verticalLayout_9.addWidget(self.rgb)
        self.gridLayout_8.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1006, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuOpen_Images = QtWidgets.QMenu(self.menuBar)
        self.menuOpen_Images.setObjectName("menuOpen_Images")
        MainWindow.setMenuBar(self.menuBar)
        self.img1 = QtWidgets.QAction(MainWindow)
        self.img1.setObjectName("img1")
        self.img2 = QtWidgets.QAction(MainWindow)
        self.img2.setObjectName("img2")
        self.menuOpen_Images.addAction(self.img1)
        self.menuOpen_Images.addAction(self.img2)
        self.menuBar.addAction(self.menuOpen_Images.menuAction())
        
        self.colorimg.ui.histogram.hide()
        self.colorimg.ui.roiBtn.hide()
        self.colorimg.ui.menuBtn.hide()
        self.colorimg.ui.roiPlot.hide()
        ####################################
        self.grayimg.ui.histogram.hide()
        self.grayimg.ui.roiBtn.hide()
        self.grayimg.ui.menuBtn.hide()
        self.grayimg.ui.roiPlot.hide()
        ####################################
        self.noise_view.ui.histogram.hide()
        self.noise_view.ui.roiBtn.hide()
        self.noise_view.ui.menuBtn.hide()
        self.noise_view.ui.roiPlot.hide()
        ###################################
        self.filter_view.ui.histogram.hide()
        self.filter_view.ui.roiBtn.hide()
        self.filter_view.ui.menuBtn.hide()
        self.filter_view.ui.roiPlot.hide()
        ####################################
        self.edge_view.ui.histogram.hide()
        self.edge_view.ui.roiBtn.hide()
        self.edge_view.ui.menuBtn.hide()
        self.edge_view.ui.roiPlot.hide()
        ##################################
        ####################################
        self.widget.ui.histogram.hide()
        self.widget.ui.roiBtn.hide()
        self.widget.ui.menuBtn.hide()
        self.widget.ui.roiPlot.hide()
        ###################################
        self.normalize_view.ui.histogram.hide()
        self.normalize_view.ui.roiBtn.hide()
        self.normalize_view.ui.menuBtn.hide()
        self.normalize_view.ui.roiPlot.hide()
        ####################################
        self.local_view.ui.histogram.hide()
        self.local_view.ui.roiBtn.hide()
        self.local_view.ui.menuBtn.hide()
        self.local_view.ui.roiPlot.hide()
        ##################################
        self.global_view.ui.histogram.hide()
        self.global_view.ui.roiBtn.hide()
        self.global_view.ui.menuBtn.hide()
        self.global_view.ui.roiPlot.hide()
        ##################################
        self.hybrid_view1.ui.histogram.hide()
        self.hybrid_view1.ui.roiBtn.hide()
        self.hybrid_view1.ui.menuBtn.hide()
        self.hybrid_view1.ui.roiPlot.hide()
        ##################################
        self.hybrid_view2.ui.histogram.hide()
        self.hybrid_view2.ui.roiBtn.hide()
        self.hybrid_view2.ui.menuBtn.hide()
        self.hybrid_view2.ui.roiPlot.hide()
        ##################################
        self.hybrid_view3.ui.histogram.hide()
        self.hybrid_view3.ui.roiBtn.hide()
        self.hybrid_view3.ui.menuBtn.hide()
        self.hybrid_view3.ui.roiPlot.hide()
        ##################################
        ##################################
        ##################################
        self.original_img.ui.histogram.hide()
        self.original_img.ui.roiBtn.hide()
        self.original_img.ui.menuBtn.hide()
        self.original_img.ui.roiPlot.hide()
        ##################################
        self.equalize_view.ui.histogram.hide()
        self.equalize_view.ui.roiBtn.hide()
        self.equalize_view.ui.menuBtn.hide()
        self.equalize_view.ui.roiPlot.hide()
        ##################################
        self.widget.ui.histogram.hide()
        self.widget.ui.roiBtn.hide()
        self.widget.ui.menuBtn.hide()
        self.widget.ui.roiPlot.hide()
        ##################################
        self.widget_2.ui.histogram.hide()
        self.widget_2.ui.roiBtn.hide()
        self.widget_2.ui.menuBtn.hide()
        self.widget_2.ui.roiPlot.hide()
        ##################################
        self.widget_5.ui.histogram.hide()
        self.widget_5.ui.roiBtn.hide()
        self.widget_5.ui.menuBtn.hide()
        self.widget_5.ui.roiPlot.hide()
        ##################################
        self.widget_3.ui.histogram.hide()
        self.widget_3.ui.roiBtn.hide()
        self.widget_3.ui.menuBtn.hide()
        self.widget_3.ui.roiPlot.hide()
        ##################################
        self.widget_4.ui.histogram.hide()
        self.widget_4.ui.roiBtn.hide()
        self.widget_4.ui.menuBtn.hide()
        self.widget_4.ui.roiPlot.hide()
        ##################################


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(6)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Computer Vision"))
        self.selectimg.setItemText(0, _translate("MainWindow", "Select Image"))
        self.selectimg.setItemText(1, _translate("MainWindow", "Image 1"))
        self.selectimg.setItemText(2, _translate("MainWindow", "Image 2"))
        self.label.setText(_translate("MainWindow", "Color Image"))
        self.label_2.setText(_translate("MainWindow", "Gray Scale Image"))
        self.tabWidget.setAccessibleName(_translate("MainWindow", "Tab "))
        self.noise.setItemText(0, _translate("MainWindow", "Adding Noise"))
        self.noise.setItemText(1, _translate("MainWindow", "Uniform Noise"))
        self.noise.setItemText(2, _translate("MainWindow", "Gaussian Noise"))
        self.noise.setItemText(3, _translate("MainWindow", "Salt & Pepper Noise"))
        self.filter.setItemText(0, _translate("MainWindow", "Apply Low Pass Filter"))
        self.filter.setItemText(1, _translate("MainWindow", "Average Filter"))
        self.filter.setItemText(2, _translate("MainWindow", "Gaussian Filter"))
        self.filter.setItemText(3, _translate("MainWindow", "Median Filter"))
        self.edge.setItemText(0, _translate("MainWindow", "Edge Detection"))
        self.edge.setItemText(1, _translate("MainWindow", "Sobel Mask"))
        self.edge.setItemText(2, _translate("MainWindow", "Roberts Mask"))
        self.edge.setItemText(3, _translate("MainWindow", "Prewitt Mask"))
        self.edge.setItemText(4, _translate("MainWindow", "Canny Mask"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MainWindow", "Tab 1"))
        self.histogram.setText(_translate("MainWindow", "Draw Histogram"))
        self.curve.setText(_translate("MainWindow", "Distribution Curve"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MainWindow", "Tab 2"))
        self.equalize.setText(_translate("MainWindow", "Equalized Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 3"))
        self.normalize.setText(_translate("MainWindow", "Normalized Image"))
        self.local_butt.setText(_translate("MainWindow", "Local Thresholding "))
        self.global_butt.setText(_translate("MainWindow", "Global Thresholding"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab4), _translate("MainWindow", "Tab 4"))
        self.hybrid.setText(_translate("MainWindow", "Hybrid Image"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab5), _translate("MainWindow", "Tab 5"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Image in Frequency Domain</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Low Pass Filter</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">High Pass Filter</p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Output Image with LPF</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Output Image with HPF</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Frequency Domian Filter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 6"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Histogram Red</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Histogram Green</p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Histogram Blue</p></body></html>"))
        self.rgb.setText(_translate("MainWindow", "Histogram RGB"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 7"))
        self.menuOpen_Images.setTitle(_translate("MainWindow", "Open Images"))
        self.img1.setText(_translate("MainWindow", "Image 1"))
        self.img2.setText(_translate("MainWindow", "Image 2"))
from pyqtgraph import ImageView, PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
