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

        self.btn = QPushButton('Расчитать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(300, 125)
        self.btn.clicked.connect(self.hello)

        self.label = QLabel(self)
        self.label.setText("ᗰนℋน ҠᗩልѢҠɣልя⍑ℴ℘")
        self.label.move(100, 10)

        self.LCD_summ = QLCDNumber(self)
        self.LCD_summ.move(110, 50)

        self.LCA_raz = QLCDNumber(self)
        self.LCA_raz.move(110, 110)

        self.LCS_delen = QLCDNumber(self)
        self.LCS_delen.move(110, 80)

        self.LCF_umn = QLCDNumber(self)
        self.LCF_umn.move(110, 140)

        self.count = 0

        self.fch = QLabel(self)
        self.fch.setText("Введите первое число: ")
        self.fch.move(240, 40)

        self.a = QLineEdit(self)
        self.a.move(360, 40)

        self.sch = QLabel(self)
        self.sch.setText("Введите второе число: ")
        self.sch.move(240, 70)

        self.b = QLineEdit(self)
        self.b.move(360, 70)

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

    def hello(self):
        a = int(self.a.text())
        b = int(self.b.text())

        if (b != 0):
            self.delen = a / b
            self.LCS_delen.display(self.delen)

            self.summ = a + b
            self.LCD_summ.display(self.summ)

            self.raz = a - b
            self.LCA_raz.display(self.raz)

            self.umn = a * b
            self.LCF_umn.display(self.umn)

        if (b == 0):
            self.delen = '-'
            self.LCS_delen.display(self.delen)

            self.summ = a + b
            self.LCD_summ.display(self.summ)

            self.raz = a - b
            self.LCA_raz.display(self.raz)

            self.umn = a * b
            self.LCF_umn.display(self.umn)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
