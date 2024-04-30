

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QThread,pyqtSignal
import random, sqlite3 as sq
import time,os


# Меню Авторизации
class Autorisation_win(object):


    def setupUi(self, Auto_win):
        Auto_win.setObjectName("Auto_win")
        Auto_win.resize(500, 450)
        Auto_win.setMinimumSize(QtCore.QSize(500, 450))
        Auto_win.setMaximumSize(QtCore.QSize(500, 450))
        Auto_win.setStyleSheet("background-color:#696969;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Auto_win)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(120, 10, 260, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_name.setFont(font)
        self.label_name.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_name.setStyleSheet("color: white;")
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 481, 331))
        self.widget.setStyleSheet("background-color: #808080;\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAcceptDrops(False)
        self.label_3.setStyleSheet("color: white;")
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit_login = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_login.setGeometry(QtCore.QRect(170, 90, 140, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_login.setFont(font)
        self.lineEdit_login.setStyleSheet("border-radius: 4px;\n"
"color: white;\n"
"transition: .2s linear;\n"
"background: #C0C0C0;\n"
"")
        self.lineEdit_login.setObjectName("lineEdit_login")
        self.label_enter = QtWidgets.QLabel(parent=self.widget)
        self.label_enter.setGeometry(QtCore.QRect(170, 30, 140, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        self.label_enter.setFont(font)
        self.label_enter.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_enter.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_enter.setObjectName("label_enter")
        self.bt_enter = QtWidgets.QPushButton(parent=self.widget)
        self.bt_enter.setGeometry(QtCore.QRect(250, 200, 140, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.bt_enter.setFont(font)
        self.bt_enter.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_enter.setMouseTracking(True)
        self.bt_enter.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:  #FFA500;")
        self.bt_enter.setObjectName("bt_enter")
        self.bt_new_ak = QtWidgets.QPushButton(parent=self.widget)
        self.bt_new_ak.setGeometry(QtCore.QRect(90, 200, 140, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_new_ak.setFont(font)
        self.bt_new_ak.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_new_ak.setMouseTracking(True)
        self.bt_new_ak.setTabletTracking(False)
        self.bt_new_ak.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_new_ak.setObjectName("bt_new_ak")
        self.lineEdit_pasword = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEdit_pasword.setGeometry(QtCore.QRect(170, 140, 140, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit_pasword.setFont(font)
        self.lineEdit_pasword.setStyleSheet("border-radius: 4px;\n"
"color: white;\n"
"transition: .2s linear;\n"
"background: #C0C0C0;\n"
"")
        self.lineEdit_pasword.setDragEnabled(True)
        self.lineEdit_pasword.setObjectName("lineEdit_pasword")
        Auto_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Auto_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        Auto_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Auto_win)
        self.statusbar.setObjectName("statusbar")
        Auto_win.setStatusBar(self.statusbar)

        Auto_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Auto_win)
        QtCore.QMetaObject.connectSlotsByName(Auto_win)
        self.func()
    def retranslateUi(self, Auto_win):
        _translate = QtCore.QCoreApplication.translate
        Auto_win.setWindowTitle(_translate("Auto_win", "Читалка"))
        self.label_name.setText(_translate("Auto_win", "Читалка"))
        self.label_3.setText(_translate("Auto_win", "Внимание! Кнопка \"Создать аккаунт\" автоматически запишет информацию как нового пользователя, вне зависимости есть ли уже аккаунт с таким именем или нет"))
        self.lineEdit_login.setPlaceholderText(_translate("Auto_win", "Логин"))
        self.label_enter.setText(_translate("Auto_win", "Вход"))
        self.bt_enter.setText(_translate("Auto_win", "Вход"))
        self.bt_new_ak.setText(_translate("Auto_win", "Создать аккаунт"))
        self.lineEdit_pasword.setPlaceholderText(_translate("Auto_win", "Пароль"))

    def func(self):
        self.bt_new_ak.clicked.connect(self.new_akk)

    def new_akk(self):
        global log, pasw
        log=self.lineEdit_login.text()
        pasw=self.lineEdit_pasword.text()
        try:
                con=sq.connect('last_auto.db')
                cur= con.cursor()
                print('done')
                cur.execute(f"INSERT INTO auto_table(login,password,score) VALUES(?, ?, ?)",(log,pasw,0))
                con.commit()
        except sq.Error as e:
                print('ERROR DATABASE')
        finally:
                con.close()




                

   




# Меню выбора режима
class Varian_of_game(object):
    def setupUi(self, Var_win):
        Var_win.setObjectName("Var_win")
        Var_win.resize(500, 450)
        Var_win.setMinimumSize(QtCore.QSize(500, 450))
        Var_win.setMaximumSize(QtCore.QSize(500, 450))
        Var_win.setStyleSheet("background-color:#696969;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Var_win)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(120, 10, 260, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_name.sizePolicy().hasHeightForWidth())
        self.label_name.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        self.label_name.setFont(font)
        self.label_name.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_name.setStyleSheet("color: white;")
        self.label_name.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 80, 481, 331))
        self.widget.setStyleSheet("background-color: #808080;\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label_change = QtWidgets.QLabel(parent=self.widget)
        self.label_change.setGeometry(QtCore.QRect(150, 30, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        self.label_change.setFont(font)
        self.label_change.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_change.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_change.setObjectName("label_change")
        self.bt_test_speed = QtWidgets.QPushButton(parent=self.widget)
        self.bt_test_speed.setGeometry(QtCore.QRect(120, 100, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.bt_test_speed.setFont(font)
        self.bt_test_speed.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_test_speed.setMouseTracking(True)
        self.bt_test_speed.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:  #FFA500;")
        self.bt_test_speed.setObjectName("bt_test_speed")
        self.bt_train_RSVP = QtWidgets.QPushButton(parent=self.widget)
        self.bt_train_RSVP.setGeometry(QtCore.QRect(120, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_train_RSVP.setFont(font)
        self.bt_train_RSVP.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_train_RSVP.setMouseTracking(True)
        self.bt_train_RSVP.setTabletTracking(False)
        self.bt_train_RSVP.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_train_RSVP.setObjectName("bt_train_RSVP")
        self.bt_train_vnima = QtWidgets.QPushButton(parent=self.widget)
        self.bt_train_vnima.setGeometry(QtCore.QRect(120, 150, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_train_vnima.setFont(font)
        self.bt_train_vnima.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_train_vnima.setMouseTracking(True)
        self.bt_train_vnima.setTabletTracking(False)
        self.bt_train_vnima.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_train_vnima.setObjectName("bt_train_vnima")
        self.bt_table = QtWidgets.QPushButton(parent=self.widget)
        self.bt_table.setGeometry(QtCore.QRect(120, 250, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_table.setFont(font)
        self.bt_table.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_table.setMouseTracking(True)
        self.bt_table.setTabletTracking(False)
        self.bt_table.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_table.setObjectName("bt_table")
        Var_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Var_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        Var_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Var_win)
        self.statusbar.setObjectName("statusbar")
        Var_win.setStatusBar(self.statusbar)

        Var_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Var_win)
        QtCore.QMetaObject.connectSlotsByName(Var_win)

    def retranslateUi(self, Var_win):
        _translate = QtCore.QCoreApplication.translate
        Var_win.setWindowTitle(_translate("Var_win", "Читалка"))
        self.label_name.setText(_translate("Var_win", "Читалка"))
        self.label_change.setText(_translate("Var_win", "Выберите режим"))
        self.bt_test_speed.setText(_translate("Var_win", "Тест скорочтения"))
        self.bt_train_RSVP.setText(_translate("Var_win", "Тренировка RSVP"))
        self.bt_train_vnima.setText(_translate("Var_win", "Тренировка внимательности"))
        self.bt_table.setText(_translate("Var_win", "Таблица лидеров"))





# Тест Скорочтения
class Starting_pack2(QThread):
        time_now=0
        item=pyqtSignal(str)

        def __init__(self):
                super().__init__()
                
                
                
        def run(self):
                self.cheak_time=0
                self.time_now=0
            
                while self.cheak_time!=-1:
                        self.time_now+=1
                        self.item.emit(str(self.time_now))
                        time.sleep(1)




class Test_speed_win(object):
    def __init__(self):
        super().__init__()    
        self.thread = Starting_pack2()
    def setupUi(self, Test_win):
        Test_win.setObjectName("Test_win")
        Test_win.resize(500, 450)
        Test_win.setMinimumSize(QtCore.QSize(500, 450))
        Test_win.setMaximumSize(QtCore.QSize(500, 450))
        Test_win.setStyleSheet("background-color:#696969;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Test_win)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 401))
        self.widget.setStyleSheet("background-color: #808080;\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label_test_speed = QtWidgets.QLabel(parent=self.widget)
        self.label_test_speed.setGeometry(QtCore.QRect(150, 30, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        self.label_test_speed.setFont(font)
        self.label_test_speed.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_test_speed.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_test_speed.setObjectName("label_test_speed")
        self.bt_start = QtWidgets.QPushButton(parent=self.widget)
        self.bt_start.setGeometry(QtCore.QRect(260, 350, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.bt_start.setFont(font)
        self.bt_start.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_start.setMouseTracking(True)
        self.bt_start.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:  #FFA500;")
        self.bt_start.setObjectName("bt_start")
        self.bt_stop = QtWidgets.QPushButton(parent=self.widget)
        self.bt_stop.setGeometry(QtCore.QRect(20, 350, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_stop.setFont(font)
        self.bt_stop.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_stop.setMouseTracking(True)
        self.bt_stop.setTabletTracking(False)
        self.bt_stop.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_stop.setObjectName("bt_stop")
        self.textEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 441, 221))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius: 4px;\n"
"color: white;\n"
"transition: .2s linear;\n"
"background: #C0C0C0;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_time = QtWidgets.QLabel(parent=self.widget)
        self.label_time.setGeometry(QtCore.QRect(20, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_time.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.bt_exit = QtWidgets.QPushButton(parent=self.widget)
        self.bt_exit.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_exit.setFont(font)
        self.bt_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_exit.setMouseTracking(True)
        self.bt_exit.setTabletTracking(False)
        self.bt_exit.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_exit.setObjectName("bt_exit")
        self.label_time_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_time_2.setGeometry(QtCore.QRect(90, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_time_2.setFont(font)
        self.label_time_2.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_time_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_time_2.setObjectName("label_time_2")
        self.label_time_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_time_3.setGeometry(QtCore.QRect(210, 70, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_time_3.setFont(font)
        self.label_time_3.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_time_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_time_3.setObjectName("label_time_3")
        self.label_time_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_time_4.setGeometry(QtCore.QRect(410, 70, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_time_4.setFont(font)
        self.label_time_4.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_time_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_time_4.setObjectName("label_time_4")
        Test_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Test_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        Test_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Test_win)
        self.statusbar.setObjectName("statusbar")
        Test_win.setStatusBar(self.statusbar)
        Test_win.setCentralWidget(self.centralwidget)
        self.retranslateUi(Test_win)
        QtCore.QMetaObject.connectSlotsByName(Test_win)
        self.func()

    def retranslateUi(self, Test_win):
        _translate = QtCore.QCoreApplication.translate
        Test_win.setWindowTitle(_translate("Test_win", "Test_win"))
        self.label_test_speed.setText(_translate("Test_win", "Тест скорочтения"))
        self.bt_start.setText(_translate("Test_win", "Старт"))
        self.bt_stop.setText(_translate("Test_win", "Стоп"))
        self.textEdit.setPlaceholderText(_translate("Test_win", "Текст для тренировки"))
        self.label_time.setText(_translate("Test_win", "Время:"))
        self.bt_exit.setText(_translate("Test_win", "Назад"))
        self.label_time_2.setText(_translate("Test_win", "00"))
        self.label_time_3.setText(_translate("Test_win", "Результат (сл/мин):"))
        self.label_time_4.setText(_translate("Test_win", "00"))
        self.thread.item.connect(self.label_time_2.setText)
    def func(self):
        self.bt_start.clicked.connect(self.Start_test)
        self.bt_stop.clicked.connect(self.Stop_test)

    def Start_test(self):
        self.thread.start()


    def Stop_test(self):
        result=1
        _translate = QtCore.QCoreApplication.translate
        self.thread.cheak_time=-1
        self.label_time_2.setText(_translate("Test_win", "00"))
        text=self.textEdit.toPlainText().split(' ')

        
        try:
            self.label_time_4.setText(_translate("Test_win",str(len(text)//self.thread.time_now)))

            con=sq.connect('last_auto.db')
            cur= con.cursor()

            cur.execute(f"UPDATE auto_table SET score={(len(text)//self.thread.time_now)} WHERE login == '{log}' ")
        
            con.commit()
        except sq.Error as e:
            print('ERROR DATABASE')
        finally:
            con.close()



class Starting_pack(QThread):
        stop_part=0
        item=pyqtSignal(str)
        def __init__(self):
                super().__init__()
                
                
                
        def run(self):

            self.stop_part=0
            list_of_words=words.split(' ')
            for x in list_of_words:
                if self.stop_part==1:
                    break
                else:
                    self.item.emit(x)
                    time.sleep(1/(speed+1))




# Тренировка по методу RSVP
class Test_RSVP_win(object):
    def __init__(self):
        super().__init__()    
        self.thread = Starting_pack()
    def setupUi(self, RSVP_win):
        RSVP_win.setObjectName("RSVP_win")
        RSVP_win.resize(500, 450)
        RSVP_win.setMinimumSize(QtCore.QSize(500, 450))
        RSVP_win.setMaximumSize(QtCore.QSize(500, 450))
        RSVP_win.setStyleSheet("background-color:#696969;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=RSVP_win)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 401))
        self.widget.setStyleSheet("background-color: #808080;\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label_RSVP = QtWidgets.QLabel(parent=self.widget)
        self.label_RSVP.setGeometry(QtCore.QRect(150, 30, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        self.label_RSVP.setFont(font)
        self.label_RSVP.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_RSVP.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_RSVP.setObjectName("label_RSVP")
        self.bt_start = QtWidgets.QPushButton(parent=self.widget)
        self.bt_start.setGeometry(QtCore.QRect(260, 350, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.bt_start.setFont(font)
        self.bt_start.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_start.setMouseTracking(True)
        self.bt_start.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:  #FFA500;")
        self.bt_start.setObjectName("bt_start")
        self.bt_stop = QtWidgets.QPushButton(parent=self.widget)
        self.bt_stop.setGeometry(QtCore.QRect(20, 350, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_stop.setFont(font)
        self.bt_stop.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_stop.setMouseTracking(True)
        self.bt_stop.setTabletTracking(False)
        self.bt_stop.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_stop.setObjectName("bt_stop")
        self.textEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.textEdit.setGeometry(QtCore.QRect(20, 160, 441, 171))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border-radius: 4px;\n"
"color: white;\n"
"transition: .2s linear;\n"
"background: #C0C0C0;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(0, 80, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.slider_speed = QtWidgets.QSlider(parent=self.widget)
        self.slider_speed.setGeometry(QtCore.QRect(140, 80, 321, 22))
        self.slider_speed.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.slider_speed.setObjectName("slider_speed")
        self.bt_exit = QtWidgets.QPushButton(parent=self.widget)
        self.bt_exit.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_exit.setFont(font)
        self.bt_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_exit.setMouseTracking(True)
        self.bt_exit.setTabletTracking(False)
        self.bt_exit.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_exit.setObjectName("bt_exit")
        self.label_RSVP_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_RSVP_2.setGeometry(QtCore.QRect(150, 110, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        self.label_RSVP_2.setFont(font)
        self.label_RSVP_2.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_RSVP_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_RSVP_2.setObjectName("label_RSVP_2")
        RSVP_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=RSVP_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        RSVP_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=RSVP_win)
        self.statusbar.setObjectName("statusbar")
        RSVP_win.setStatusBar(self.statusbar)
        RSVP_win.setCentralWidget(self.centralwidget)
        self.retranslateUi(RSVP_win)
        QtCore.QMetaObject.connectSlotsByName(RSVP_win)
        self.func()
    def retranslateUi(self, RSVP_win):
        _translate = QtCore.QCoreApplication.translate
        RSVP_win.setWindowTitle(_translate("RSVP_win", "RSVP_win"))
        self.label_RSVP.setText(_translate("RSVP_win", "RSVP"))
        self.bt_start.setText(_translate("RSVP_win", "Старт"))
        self.bt_stop.setText(_translate("RSVP_win", "Стоп"))
        self.textEdit.setPlaceholderText(_translate("RSVP_win", "Текст для тренировки"))
        self.label_4.setText(_translate("RSVP_win", "Скорость"))
        self.bt_exit.setText(_translate("RSVP_win", "Назад"))
        self.label_RSVP_2.setText(_translate("RSVP_win", "..."))
        self.thread.item.connect(self.label_RSVP_2.setText)


    def func(self):
        self.bt_start.clicked.connect(self.Start_RSVP_test)
        self.bt_stop.clicked.connect(self.Stop_RSVP_test)

    def Start_RSVP_test(self):
        global words,speed
        words=self.textEdit.toPlainText()
        speed=self.slider_speed.value()
        
        self.thread.start()


    def Stop_RSVP_test(self):
        _translate = QtCore.QCoreApplication.translate
        self.thread.stop_part=1
        self.label_RSVP_2.setText(_translate("RSVP_win", "..."))



# Тренировка внимательности
class Starting_pack1(QThread):
        stop_part=0
        item1=pyqtSignal(str)
        item2=pyqtSignal(str)
        item3=pyqtSignal(str)
        def __init__(self):
                super().__init__()


        def run(self):
            time.sleep(1)
            self.item1.emit(find_of_words[int(now_posit[0])])
            self.item2.emit(find_of_words[int(now_posit[1])])
            self.item3.emit(find_of_words[int(now_posit[2])])
            time.sleep(1)
            self.item1.emit("...")
            self.item2.emit("...")
            self.item3.emit("...")



class Train_vnimatel_win(object):
    def __init__(self):
        super().__init__()    
        self.thread = Starting_pack1()
    def setupUi(self, Train_vn_win):
        Train_vn_win.setObjectName("Train_vn_win")
        Train_vn_win.resize(500, 450)
        Train_vn_win.setMinimumSize(QtCore.QSize(500, 450))
        Train_vn_win.setMaximumSize(QtCore.QSize(500, 450))
        Train_vn_win.setStyleSheet("background-color:#696969;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Train_vn_win)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 421))
        self.widget.setStyleSheet("background-color: #808080;\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label_test_vnima = QtWidgets.QLabel(parent=self.widget)
        self.label_test_vnima.setGeometry(QtCore.QRect(40, 40, 400, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        self.label_test_vnima.setFont(font)
        self.label_test_vnima.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_test_vnima.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_test_vnima.setObjectName("label_test_vnima")
        self.bt_cheak = QtWidgets.QPushButton(parent=self.widget)
        self.bt_cheak.setGeometry(QtCore.QRect(329, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        self.bt_cheak.setFont(font)
        self.bt_cheak.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_cheak.setMouseTracking(True)
        self.bt_cheak.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:  #FFA500;")
        self.bt_cheak.setObjectName("bt_cheak")
        self.bt_reset = QtWidgets.QPushButton(parent=self.widget)
        self.bt_reset.setGeometry(QtCore.QRect(20, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_reset.setFont(font)
        self.bt_reset.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_reset.setMouseTracking(True)
        self.bt_reset.setTabletTracking(False)
        self.bt_reset.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_reset.setObjectName("bt_reset")
        self.bt_exit = QtWidgets.QPushButton(parent=self.widget)
        self.bt_exit.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_exit.setFont(font)
        self.bt_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_exit.setMouseTracking(True)
        self.bt_exit.setTabletTracking(False)
        self.bt_exit.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_exit.setObjectName("bt_exit")
        self.label_1 = QtWidgets.QLabel(parent=self.widget)
        self.label_1.setGeometry(QtCore.QRect(20, 150, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(175, 150, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(330, 150, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_text_num = QtWidgets.QLabel(parent=self.widget)
        self.label_text_num.setGeometry(QtCore.QRect(20, 210, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_text_num.setFont(font)
        self.label_text_num.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_text_num.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_text_num.setObjectName("label_text_num")
        self.bt_start = QtWidgets.QPushButton(parent=self.widget)
        self.bt_start.setGeometry(QtCore.QRect(175, 350, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_start.setFont(font)
        self.bt_start.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_start.setMouseTracking(True)
        self.bt_start.setTabletTracking(False)
        self.bt_start.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_start.setObjectName("bt_start")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 441, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.spinBox = QtWidgets.QSpinBox(parent=self.widget)
        self.spinBox.setGeometry(QtCore.QRect(290, 200, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("color: white;")
        self.spinBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(3)
        self.spinBox.setSingleStep(1)
        self.spinBox.setObjectName("spinBox")
        Train_vn_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Train_vn_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        Train_vn_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Train_vn_win)
        self.statusbar.setObjectName("statusbar")
        Train_vn_win.setStatusBar(self.statusbar)

        Train_vn_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Train_vn_win)
        QtCore.QMetaObject.connectSlotsByName(Train_vn_win)
        self.func()
    def retranslateUi(self, Train_vn_win):
        _translate = QtCore.QCoreApplication.translate
        Train_vn_win.setWindowTitle(_translate("Train_vn_win", "Читалка"))
        self.label_test_vnima.setText(_translate("Train_vn_win", "Тренировка внимательности"))
        self.bt_cheak.setText(_translate("Train_vn_win", "Проверить"))
        self.bt_reset.setText(_translate("Train_vn_win", "Обновить слово"))
        self.bt_exit.setText(_translate("Train_vn_win", "Назад"))
        self.label_1.setText(_translate("Train_vn_win", "..."))
        self.label_2.setText(_translate("Train_vn_win", "..."))
        self.label_3.setText(_translate("Train_vn_win", "..."))
        self.label_text_num.setText(_translate("Train_vn_win", "Нужное слово под номером:"))
        self.bt_start.setText(_translate("Train_vn_win", "Запуск"))
        self.label_8.setText(_translate("Train_vn_win", "Найди слово: ..."))
        self.thread.item1.connect(self.label_1.setText)
        self.thread.item2.connect(self.label_2.setText)
        self.thread.item3.connect(self.label_3.setText)
    def func(self):
        self.bt_start.clicked.connect(self.Start_test)
        self.bt_reset.clicked.connect(self.Reset_test)
        self.bt_cheak.clicked.connect(self.Cheak_test)

    def Start_test(self):
        _translate = QtCore.QCoreApplication.translate
        global Win_word,now_posit,Win_number,find_of_words
        find_of_words_co=[['Вопрос','Время','Вид'],['Глаз','Год','Голова'],['Дело','День','Дом'],['Место','Мир','Работа'],['Раз','Ребенок','Рука'],['Сила','Слово','Случай']]
        find_of_words=find_of_words_co[random.randrange(0,6,1)]
        position=['012','021','102','120','201','210']
        now_posit=str(position[random.randrange(0,6,1)])
        Win_word=find_of_words[random.randrange(0,3,1)]
        self.label_8.setText(_translate("Train_vn_win", "Найди слово: "+Win_word))
        Win_number=int(now_posit[find_of_words.index(Win_word)])

        self.thread.start()

        




    def Reset_test(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("Train_vn_win", "Найди слово: ..."))
        self.label_1.setText(_translate("Train_vn_win", "..."))
        self.label_2.setText(_translate("Train_vn_win", "..."))
        self.label_3.setText(_translate("Train_vn_win", "..."))

    def Cheak_test(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("Train_vn_win", "Найди слово: ..."))
        if Win_number == (self.spinBox.value()-1):
            self.label_8.setText(_translate("Train_vn_win", "Победа"))
        else:
            self.label_8.setText(_translate("Train_vn_win", "Поражение"))

# Таблица лидеров
class Table_of_liders_win(object):
    def setupUi(self, Table_win):
        Table_win.setObjectName("Table_win")
        Table_win.resize(500, 450)
        Table_win.setMinimumSize(QtCore.QSize(500, 450))
        Table_win.setMaximumSize(QtCore.QSize(500, 450))
        Table_win.setStyleSheet("background-color:#696969;\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=Table_win)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 421))
        self.widget.setStyleSheet("background-color: #808080;\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.label_RSVP = QtWidgets.QLabel(parent=self.widget)
        self.label_RSVP.setGeometry(QtCore.QRect(150, 30, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        self.label_RSVP.setFont(font)
        self.label_RSVP.setStyleSheet("background-color: #808080;\n"
"color: white;")
        self.label_RSVP.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_RSVP.setObjectName("label_RSVP")
        self.bt_exit = QtWidgets.QPushButton(parent=self.widget)
        self.bt_exit.setGeometry(QtCore.QRect(20, 10, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.bt_exit.setFont(font)
        self.bt_exit.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.bt_exit.setMouseTracking(True)
        self.bt_exit.setTabletTracking(False)
        self.bt_exit.setStyleSheet("border-radius: 10px;\n"
"color: white;\n"
" transition: .2s linear;\n"
"background:#A9A9A9;\n"
"\n"
"")
        self.bt_exit.setObjectName("bt_exit")
        self.listWidget = QtWidgets.QListWidget(parent=self.widget)
        self.listWidget.setGeometry(QtCore.QRect(30, 80, 221, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("color: white")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(parent=self.widget)
        self.listWidget_2.setGeometry(QtCore.QRect(250, 80, 221, 301))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("color: white")
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        Table_win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Table_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        Table_win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Table_win)
        self.statusbar.setObjectName("statusbar")
        Table_win.setStatusBar(self.statusbar)

        Table_win.setCentralWidget(self.centralwidget)

        self.retranslateUi(Table_win)
        QtCore.QMetaObject.connectSlotsByName(Table_win)

    def retranslateUi(self, Table_win):
        try:
                con=sq.connect('last_auto.db')
                cur= con.cursor()

                cur.execute("SELECT login, score FROM auto_table ORDER BY score DESC LIMIT 5")
                a=[]
                for r in cur:
                        for x in r:
                                a.append(x)
                con.commit()
                print(a)
        except sq.Error as e:
                print('ERROR DATABASE')
        finally:
                con.close()
        
        
        _translate = QtCore.QCoreApplication.translate
        Table_win.setWindowTitle(_translate("Table_win", "Читалка"))
        self.label_RSVP.setText(_translate("Table_win", "Таблица лидеров"))
        self.bt_exit.setText(_translate("Table_win", "Назад"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)

        try:
                item = self.listWidget.item(0)
                item.setText(_translate("MainWindow", "1. "+a[0]))
        except:
                item = self.listWidget.item(0)
                item.setText(_translate("MainWindow", "1. -"))
        try:
                item = self.listWidget.item(1)
                item.setText(_translate("MainWindow", "2. "+a[2]))
        except:
                item = self.listWidget.item(1)
                item.setText(_translate("MainWindow", "2. -"))
        try:
                item = self.listWidget.item(2)
                item.setText(_translate("MainWindow", "3. "+a[4]))
        except:
                item = self.listWidget.item(2)
                item.setText(_translate("MainWindow", "3. -"))
        try:
                item = self.listWidget.item(3)
                item.setText(_translate("MainWindow", "4. "+a[6]))
        except:
                item = self.listWidget.item(3)
                item.setText(_translate("MainWindow", "4. -"))
        try:
                item = self.listWidget.item(4)
                item.setText(_translate("MainWindow", "5. "+a[8]))
        except:
                item = self.listWidget.item(4)
                item.setText(_translate("MainWindow", "5. -"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        try:
                item = self.listWidget_2.item(0)
                item.setText(_translate("MainWindow", str(a[1])))
        except:
                item = self.listWidget_2.item(0)
                item.setText(_translate("MainWindow", "-"))
        try:
                item = self.listWidget_2.item(1)
                item.setText(_translate("MainWindow", str(a[3])))
        except:
                item = self.listWidget_2.item(1)
                item.setText(_translate("MainWindow", "-"))
        try:
                item = self.listWidget_2.item(2)
                item.setText(_translate("MainWindow", str(a[5])))
        except:
                item = self.listWidget_2.item(2)
                item.setText(_translate("MainWindow", "-"))
        try:
                item = self.listWidget_2.item(3)
                item.setText(_translate("MainWindow", str(a[7])))
        except:
                item = self.listWidget_2.item(3)
                item.setText(_translate("MainWindow", "-"))
        try:
                item = self.listWidget_2.item(4)
                item.setText(_translate("MainWindow", str(a[9])))
        except:
                item = self.listWidget_2.item(4)
                item.setText(_translate("MainWindow", "-"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)






class Auto_win(QtWidgets.QMainWindow, Autorisation_win):
    def __init__(self, parent = None):
        super(Auto_win, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.stacked = self.parent.stacked
        print('asd')
        self.bt_enter.clicked.connect(self.run)
    def run(self):   
        global log
        log=self.lineEdit_login.text()
        try:
                con=sq.connect('last_auto.db')
                cur= con.cursor()
                print('done')
                cur.execute(f"SELECT password FROM auto_table WHERE login == '{log}'")
                print(cur)
                a=[]
                for r in cur:
                        for x in r:
                                a.append(x)
                print(a)
                con.commit()
                if a[0] == self.lineEdit_pasword.text():
                     
                        self.stacked.setCurrentIndex(1)
        except sq.Error as e:
                print('ERROR DATABASE')
        finally:
                con.close()
        


                

        

class Var_win(QtWidgets.QMainWindow, Varian_of_game):
    def __init__(self, parent = None):
        super(Var_win, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.stacked = self.parent.stacked

        self.bt_test_speed.clicked.connect(lambda : self.stacked.setCurrentIndex(2))
        self.bt_train_RSVP.clicked.connect(lambda : self.stacked.setCurrentIndex(3))
        self.bt_train_vnima.clicked.connect(lambda : self.stacked.setCurrentIndex(4))
        self.bt_table.clicked.connect(lambda : self.stacked.setCurrentIndex(5))

class Test_win(QtWidgets.QMainWindow, Test_speed_win):
    def __init__(self, parent = None):
        super(Test_win, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.stacked = self.parent.stacked

        self.bt_exit.clicked.connect(lambda : self.stacked.setCurrentIndex(1))


class RSVP_win(QtWidgets.QMainWindow, Test_RSVP_win):
    def __init__(self, parent = None):
        super(RSVP_win, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.stacked = self.parent.stacked


        self.bt_exit.clicked.connect(lambda : self.stacked.setCurrentIndex(1))

class Train_vn_win(QtWidgets.QMainWindow, Train_vnimatel_win):
    def __init__(self, parent = None):
        super(Train_vn_win, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.stacked = self.parent.stacked

        self.bt_exit.clicked.connect(lambda : self.stacked.setCurrentIndex(1))
class Table_win(QtWidgets.QMainWindow, Table_of_liders_win):
    def __init__(self, parent = None):
        super(Table_win, self).__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.stacked = self.parent.stacked

        self.bt_exit.clicked.connect(lambda : self.stacked.setCurrentIndex(1))

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()


        self.stacked = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked)

        self.Window_Win1 = Auto_win(self)
        self.Window_Win2 = Var_win(self)
        self.Window_Win3 = Test_win(self)
        self.Window_Win4 = RSVP_win(self)
        self.Window_Win5 = Train_vn_win(self)
        self.Window_Win6 = Table_win(self)

        self.stacked.addWidget(self.Window_Win1)
        self.stacked.addWidget(self.Window_Win2)
        self.stacked.addWidget(self.Window_Win3)
        self.stacked.addWidget(self.Window_Win4)
        self.stacked.addWidget(self.Window_Win5)
        self.stacked.addWidget(self.Window_Win6)
        
        
    
        
    
        


if __name__ == "__main__":

    from sys import argv, exit
    app = QtWidgets.QApplication(argv)
    app.setWindowIcon(QtGui.QIcon('png_icon.png'))
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon('png_icon.png'))
    window.setWindowTitle('Читалка')  
    if os.path.isfile("last_auto.db"):
        pass
    else:
        f=open('last_auto.db', 'w')
        f.close()
    try:
        con=sq.connect('last_auto.db')
        cur= con.cursor()
        print('done')
        cur.execute(f"CREATE TABLE IF NOT EXISTS auto_table(login TEXT NOT NULL, password TEXT NOT NULL, score INTEGER NOT NULL DEFAULT 0)")
        con.commit()
    except sq.Error as e:
        print('ERROR DATABASE')
    finally:
        con.close()
    window.show()
    exit(app.exec())

    
