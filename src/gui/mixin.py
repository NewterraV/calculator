from PyQt5.QtWidgets import QMessageBox

class CalcFuncMixin(object):

    def __init__(self):
        self.label = None
        self.is_equal = None

    def write_number(self, number: str):
        if self.is_equal and number in "^+-*/.":
            self.label.setText(self.label.text() + number)
            self.is_equal = False
        elif self.label.text() == "0" and number in "/.":
            self.label.setText(self.label.text() + number)
        elif self.label.text() == "0" or self.is_equal:
            self.label.setText(number)
            self.is_equal = False
        else:
            self.label.setText(self.label.text() + number)

    def clean(self):
        self.label.setText("0")

    def del_one(self):
        if self.label.text() == "0":
            return
        elif len(self.label.text()) == 1:
            self.label.setText("0")
        else:
            self.label.setText(self.label.text()[0: -1])

    def equals(self):
        try:
            if "^" in self.label.text():
                self.label.setText(self.label.text().replace("^", "**"))
            res = eval(self.label.text())
            res = (
                str(round(res, 3))
                if type(res) is float
                else str(res)
            )
            if res[-2:] == ".0":
                res = res[0:-2]
            self.label.setText(res)
            self.is_equal = True
        except ZeroDivisionError:
            self.err_division_zero()

    @staticmethod
    def err_division_zero():
        """Ошибка деления на ноль"""
        err = QMessageBox()
        err.setWindowTitle("Ошибка")
        err.setText("На ноль делить нельзя")
        err.setIcon(QMessageBox.Warning)
        err.setStandardButtons(QMessageBox.Ok)

        err.exec_()
