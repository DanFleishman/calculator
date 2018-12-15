import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber, QLineEdit
import math


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle('Пятая программа')

        # self.btn = QPushButton('Расчитать', self)
        # self.btn.resize(self.btn.sizeHint())
        # self.btn.move(300, 125)
        # self.btn.clicked.connect(self.hello)

        self.nol = QPushButton('0', self)
        self.nol.resize(self.nol.sizeHint())
        self.nol.move(300, 140)
        self.nol.clicked.connect(self.no)

        self.umn = QPushButton('*', self)
        self.umn.resize(self.umn.sizeHint())
        self.umn.move(200, 170)
        self.umn.clicked.connect(self.umno)

        self.minu = QPushButton('-', self)
        self.minu.resize(self.minu.sizeHint())
        self.minu.move(500, 170)
        self.minu.clicked.connect(self.minus)

        self.plu = QPushButton('+', self)
        self.plu.resize(self.plu.sizeHint())
        self.plu.move(300, 170)
        self.plu.clicked.connect(self.plus)

        self.deleni = QPushButton('/', self)
        self.deleni.resize(self.deleni.sizeHint())
        self.deleni.move(400, 170)
        self.deleni.clicked.connect(self.delenie)

        self.fact = QPushButton('!', self)
        self.fact.resize(self.fact.sizeHint())
        self.fact.move(300, 200)
        self.fact.clicked.connect(self.factorial)

        self.kor = QPushButton('√', self)
        self.kor.resize(self.kor.sizeHint())
        self.kor.move(200, 200)
        self.kor.clicked.connect(self.koren)

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

        self.clean = QPushButton('C', self)
        self.clean.resize(self.shest.sizeHint())
        self.clean.move(200, 140)
        self.clean.clicked.connect(self.c)

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

        self.ent = QPushButton('Enter', self)
        self.ent.resize(self.ent.sizeHint())
        self.ent.move(400, 140)
        self.ent.clicked.connect(self.en)

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

        self.LCK_kor = QLCDNumber(self)
        self.LCK_kor.move(110, 170)

        self.LCFa_fact = QLCDNumber(self)
        self.LCFa_fact.move(110, 200)

        self.count = 0

        self.qw = 0

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

        self.chisla=[]


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

        self.k = QLabel(self)
        self.k.setText("Корень:")
        self.k.move(5, 170)

        self.f = QLabel(self)
        self.f.setText("Факториал:")
        self.f.move(5, 200)

        self.fch = QLabel(self)
        self.fch.move(40,30)

    def umno(self):
        self.LCF_umn.display(int(self.chisla[0])*int(self.chisla[1]))

    def minus(self):
        self.LCA_raz.display(int(self.chisla[0])-int(self.chisla[1]))

    def plus(self):
        self.LCD_summ.display(int(self.chisla[0])+int(self.chisla[1]))

    def delenie(self):
        self.LCS_delen.display(int(self.chisla[0])/int(self.chisla[1]))

    def koren(self):

        self.LCK_kor.display(math.sqrt(int(self.chisla[0])))

    def factorial(self):
         self.LCFa_fact.display(math.factorial(int(self.chisla[0])))


    def c(self):
        self.chisla = []
        self.su = []
        self.fch.setText('')
        self.LCF_umn.display(self.qw)
        self.LCA_raz.display(self.qw)
        self.LCS_delen.display(self.qw)
        self.LCD_summ.display(self.qw)
        self.LCK_kor.display(self.qw)
        self.LCFa_fact.display(self.qw)


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


    def en(self):
        self.chisla.append(''.join(self.su))
        self.su=[]
        self.fch.setText('')

    # def c(self):
    #     self.chisla=[]
    #     self.su=[]
    #     self.fch.setText('')
    #     self.LCF_umn.display(self.qw)


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
