import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 500, 200)
        self.setWindowTitle('Пятая программа')

        # self.btn = QPushButton('Расчитать', self)
        # self.btn.resize(self.btn.sizeHint())
        # self.btn.move(300, 125)
        # self.btn.clicked.connect(self.hello)

        self.nol = QPushButton('0', self)
        self.nol.resize(self.nol.sizeHint())
        self.nol.move(300, 140)
        self.nol.clicked.connect(self.no)

        self.odin = QPushButton('1', self)
        self.odin.resize(self.odin.sizeHint())
        self.odin.move(200, 50)
        self.odin.clicked.connect(self.od)

        self.two = QPushButton('2', self)
        self.two.resize(self.two.sizeHint())
        self.two.move(300, 50)
        self.two.clicked.connect(self.dv)

        self.three = QPushButton('3', self)
        self.three.resize(self.three.sizeHint())
        self.three.move(400, 50)
        self.three.clicked.connect(self.tr)

        self.four = QPushButton('4', self)
        self.four.resize(self.four.sizeHint())
        self.four.move(200, 80)
        self.four.clicked.connect(self.ch)

        self.pyat = QPushButton('5', self)
        self.pyat.resize(self.pyat.sizeHint())
        self.pyat.move(300, 80)
        self.pyat.clicked.connect(self.py)

        self.shest = QPushButton('6', self)
        self.shest.resize(self.shest.sizeHint())
        self.shest.move(400, 80)
        self.shest.clicked.connect(self.sh)

        self.sem = QPushButton('7', self)
        self.sem.resize(self.sem.sizeHint())
        self.sem.move(200, 110)
        self.sem.clicked.connect(self.se)

        self.vosem = QPushButton('8', self)
        self.vosem.resize(self.vosem.sizeHint())
        self.vosem.move(300, 110)
        self.vosem.clicked.connect(self.vo)

        self.deviat = QPushButton('9', self)
        self.deviat.resize(self.deviat.sizeHint())
        self.deviat.move(400, 110)
        self.deviat.clicked.connect(self.de)

        self.label = QLabel(self)
        self.label.setText("ᗰนℋน ҠᗩልѢҠɣልя⍑ℴ℘")
        self.label.move(300, 10)

        self.LCD_summ = QLCDNumber(self)
        self.LCD_summ.move(110, 50)

        self.LCA_raz = QLCDNumber(self)
        self.LCA_raz.move(110, 110)

        self.LCS_delen = QLCDNumber(self)
        self.LCS_delen.move(110, 80)

        self.LCF_umn = QLCDNumber(self)
        self.LCF_umn.move(110, 140)

        self.count = 0

        #self.fch = QLabel(self)
        #self.fch.setText("Введите первое число: ")
        #self.fch.move(240, 40)

        #self.a = QLineEdit(self)
        #self.a.move(360, 40)

        #self.sch = QLabel(self)
        #self.sch.setText("Введите второе число: ")
        #self.sch.move(240, 70)

        #self.b = QLineEdit(self)
        #self.b.move(360, 70)
        self.t = 1

        self.su = []

        self.x = 40


        self.s = QLabel(self)
        self.s.setText("Сумма:")
        self.s.move(5, 50)

        self.d = QLabel(self)
        self.d.setText("Деление:")
        self.d.move(5, 80)

        self.r = QLabel(self)
        self.r.setText("Разница:")
        self.r.move(5, 110)

        self.u = QLabel(self)
        self.u.setText("Умножение:")
        self.u.move(5, 140)

        self.fch = QLabel(self)
        self.fch.move(40,30)

    def no(self):

        self.su.append('0')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()


    def od(self):

        self.su.append('1')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()


    def dv(self):

        self.su.append('2')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()


    def tr(self):

        self.su.append('3')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()


    def ch(self):

        self.su.append('4')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()


    def py(self):

        self.su.append('5')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()

    def sh(self):

        self.su.append('6')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()


    def se(self):

        self.su.append('7')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()

    def vo(self):

        self.su.append('8')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()

    def de(self):

        self.su.append('9')
        self.fch.setText(''.join(self.su))
        self.fch.adjustSize()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
