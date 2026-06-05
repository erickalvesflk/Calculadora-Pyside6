"""
    ARQUIVO PYTHON PRINCIPAL DO SOFTWARE
"""
import sys,gc
from utils.qtcore import *
from utils.path import *
from utils.config import *
from gui.styles.styles import style_list, reload_theme
from gui.windows.uimainwindow import UiMainWindow
from app.system import CalcSystem

res = False

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.ui = UiMainWindow(self)
        self.system = CalcSystem()
        self.config = False
        self.usingQCombo = False

        self.ui.btn_0.clicked.connect(lambda: self.add_and_update_label("0"))
        self.ui.btn_1.clicked.connect(lambda: self.add_and_update_label("1"))
        self.ui.btn_2.clicked.connect(lambda: self.add_and_update_label("2"))
        self.ui.btn_3.clicked.connect(lambda: self.add_and_update_label("3"))
        self.ui.btn_4.clicked.connect(lambda: self.add_and_update_label("4"))
        self.ui.btn_5.clicked.connect(lambda: self.add_and_update_label("5"))
        self.ui.btn_6.clicked.connect(lambda: self.add_and_update_label("6"))
        self.ui.btn_7.clicked.connect(lambda: self.add_and_update_label("7"))
        self.ui.btn_8.clicked.connect(lambda: self.add_and_update_label("8"))
        self.ui.btn_9.clicked.connect(lambda: self.add_and_update_label("9"))
        self.ui.btn_point.clicked.connect(lambda: self.add_and_update_label("."))

        self.ui.btn_plus.clicked.connect(lambda: self.add_and_update_label("+"))
        self.ui.btn_less.clicked.connect(lambda: self.add_and_update_label("-"))
        self.ui.btn_multi.clicked.connect(lambda: self.add_and_update_label("x"))
        self.ui.btn_division.clicked.connect(lambda: self.add_and_update_label("÷"))
        self.ui.btn_mod.clicked.connect(lambda: self.add_and_update_label("mod"))
        self.ui.btn_p.clicked.connect(lambda: self.add_and_update_label("()"))
        self.ui.btn_equal.clicked.connect(self.result_and_update_label)

        self.ui.btn_ac.clicked.connect(self.reset_and_update_label)
        self.ui.btn_del.clicked.connect(self.del_and_update_label)

        self.ui.themes_options.currentTextChanged.connect(self.chage_style)

    def keyPressEvent(self,event : QKeyEvent):
        key = event.key()
        c = event.text()
        
        if (key == Qt.Key.Key_Escape) and self.ui.config_frame.pos().x() in [0,-CONFIG_SIZE]:
            # Animação

            self.animation = QPropertyAnimation(self.ui.config_frame,b"pos")
            self.animation.setDuration(300)
            self.animation.setEasingCurve(QEasingCurve.Type.InOutCirc)
            if not self.config:
                self.animation.setStartValue(QPoint(-CONFIG_SIZE, 0))
                self.animation.setEndValue(QPoint(0, 0))
                self.config = True
            else:
                self.animation.setStartValue(QPoint(0, 0))
                self.animation.setEndValue(QPoint(-CONFIG_SIZE, 0))
                self.config = False

            self.animation.start()
            return

        table_chars = {
            "+": self.ui.btn_plus,
            "*": self.ui.btn_multi, 
            "%": self.ui.btn_mod,
            "(": self.ui.btn_p,
            ")": self.ui.btn_p,
        }
    
        if c in table_chars:
            table_chars[c].click()
            return # Finaliza o evento aqui se for um desses caracteres

        table_btns = {
            Qt.Key.Key_0: self.ui.btn_0,
            Qt.Key.Key_1: self.ui.btn_1,
            Qt.Key.Key_2: self.ui.btn_2,
            Qt.Key.Key_3: self.ui.btn_3,
            Qt.Key.Key_4: self.ui.btn_4,
            Qt.Key.Key_5: self.ui.btn_5,
            Qt.Key.Key_6: self.ui.btn_6,
            Qt.Key.Key_7: self.ui.btn_7,
            Qt.Key.Key_9: self.ui.btn_9,
            Qt.Key.Key_Period: self.ui.btn_point,
            Qt.Key.Key_Backspace: self.ui.btn_del,
            Qt.Key.Key_Slash : self.ui.btn_division,
            Qt.Key.Key_Minus : self.ui.btn_less,
            Qt.Key.Key_Equal: self.ui.btn_equal,
            Qt.Key.Key_Return: self.ui.btn_equal,
        }
  
        try:
            table_btns[key].click()
        except KeyError:
            pass

    def chage_style(self, theme_name: str):
        reload_theme(theme_name)

    def add_and_update_label(self,n:str) -> None:
        self.ui.display_label.setText(self.system.add_to_op(n))

    def reset_and_update_label(self) -> None:
        self.ui.display_label.setText(self.system.reset())

    def del_and_update_label(self) -> None:
        self.ui.display_label.setText(self.system.delete_c())

    def result_and_update_label(self) -> None:
        self.ui.display_label.setText(self.system.result())
        QTimer.singleShot(1000,lambda: self.ui.display_label.setText(self.system.label))

def open_app():

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    app.shutdown()
    del app

if __name__ == "__main__":
    restart = False

    open_app()

    sys.exit()