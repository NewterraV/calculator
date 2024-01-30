from PyQt5 import QtCore, QtGui, QtWidgets
from .mixin import CalcFuncMixin


class Ui_MainWindow(CalcFuncMixin):

    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 599)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.__set_label()
        self.__set_btn_0()
        self.__set_btn_1()
        self.__set_btn_2()
        self.__set_btn_3()
        self.__set_btn_4()
        self.__set_btn_5()
        self.__set_btn_6()
        self.__set_btn_7()
        self.__set_btn_8()
        self.__set_btn_9()
        self.__set_btn_dot()
        self.__set_btn_func()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.is_equal = False

    def __set_label(self):
        """Конструктор поля с текстом"""
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(False)
        self.label.setTabletTracking(False)
        self.label.setStyleSheet("background-color: rgb(246, 245, 244);\n"
                                 "border-color: rgb(119, 118, 123);")
        self.label.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")

    def __set_btn_0(self):
        """Конструктор кнопки 0"""
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.btn_0.clicked.connect(
            lambda: self.write_number(self.btn_0.text()))

    def __set_btn_1(self):
        """Конструктор кнопки 1"""
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_1.clicked.connect(
            lambda: self.write_number(self.btn_1.text()))


    def __set_btn_2(self):
        """Конструктор кнопки 2"""
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_2.clicked.connect(
            lambda: self.write_number(self.btn_2.text()))

    def __set_btn_3(self):
        """Конструктор кнопки 3"""
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_3.clicked.connect(
            lambda: self.write_number(self.btn_3.text()))

    def __set_btn_4(self):
        """Конструктор кнопки 4"""
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_4.clicked.connect(
            lambda: self.write_number(self.btn_4.text()))

    def __set_btn_5(self):
        """Конструктор кнопки 5"""
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_5.clicked.connect(
            lambda: self.write_number(self.btn_5.text()))


    def __set_btn_6(self):
        """Конструктор кнопки 6"""
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_6.clicked.connect(
            lambda: self.write_number(self.btn_6.text()))

    def __set_btn_7(self):
        """Конструктор кнопки 7"""
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.btn_7.clicked.connect(
            lambda: self.write_number(self.btn_7.text()))

    def __set_btn_8(self):
        """Конструктор кнопки 8"""
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.btn_8.clicked.connect(
            lambda: self.write_number(self.btn_8.text()))

    def __set_btn_9(self):
        """Конструктор кнопки 9"""
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_9.clicked.connect(
            lambda: self.write_number(self.btn_9.text()))

    def __set_btn_dot(self):
        """Конструктор кнопки точка"""
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dot.setGeometry(QtCore.QRect(100, 500, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.btn_dot.clicked.connect(
            lambda: self.write_number(self.btn_dot.text()))


    def __set_btn_func(self):
        """Конструктор функциональных кнопок"""

        self.btn_eq = QtWidgets.QPushButton(self.centralwidget)
        self.btn_eq.setGeometry(QtCore.QRect(200, 500, 201, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_eq.setFont(font)
        self.btn_eq.setObjectName("btn_eq")
        self.btn_eq.clicked.connect(lambda: self.equals())

        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(300, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_plus.clicked.connect(
            lambda: self.write_number(self.btn_plus.text()))

        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(300, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.btn_minus.clicked.connect(
            lambda: self.write_number(self.btn_minus.text()))

        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(300, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.btn_div.clicked.connect(
            lambda: self.write_number(self.btn_div.text()))

        self.btn_multip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multip.setGeometry(QtCore.QRect(300, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_multip.setFont(font)
        self.btn_multip.setObjectName("btn_multip")
        self.btn_multip.clicked.connect(
            lambda: self.write_number(self.btn_multip.text()))

        self.btn_dg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dg.setGeometry(QtCore.QRect(200, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_dg.setFont(font)
        self.btn_dg.setObjectName("btn_dg")
        self.btn_dg.clicked.connect(
            lambda: self.write_number(self.btn_multip_2.text()))

        self.btn_bs = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bs.setGeometry(QtCore.QRect(100, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.btn_bs.setFont(font)
        self.btn_bs.setObjectName("btn_bs")
        self.btn_bs.clicked.connect(lambda: self.del_one())

        self.btn_ce = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ce.setGeometry(QtCore.QRect(0, 100, 100, 100))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Condensed")
        font.setPointSize(45)
        self.btn_ce.setFont(font)
        self.btn_ce.setObjectName("btn_ce")
        self.btn_ce.clicked.connect(lambda: self.clean())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_eq.setText(_translate("MainWindow", "="))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_multip.setText(_translate("MainWindow", "*"))
        self.btn_dg.setText(_translate("MainWindow", "^"))
        self.btn_bs.setText(_translate("MainWindow", "<-"))
        self.btn_ce.setText(_translate("MainWindow", "CE"))
        self.btn_dot.setText(_translate("MainWindow", "."))
