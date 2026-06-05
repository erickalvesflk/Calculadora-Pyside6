from utils.qtcore import *
from gui.styles.styles import getTheme

theme = getTheme()
buttonsize = 49

class NormalButton(QPushButton):
    """
    Classe que cria um botão QPushButton personalizado para a calculadora
    """
    def __init__(
            self,
            text : str,
            width = buttonsize,
            height = buttonsize,
    ):
        super().__init__()
        self.setText(text)
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        self.setStyleSheet(theme.getStyleSheet("QPushButtonNormal"))

class SpecialButton(QPushButton):
    """
    Classe que cria um botão QPushButton personalizado para a calculadora (Especial)
    """
    def __init__(
            self,
            text : str,
            width = buttonsize,
            height = buttonsize,
    ):
        super().__init__()
        self.setText(text)
        self.setMinimumWidth(width)
        self.setMaximumWidth(width)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)
        self.setStyleSheet(theme.getStyleSheet("QPushButtonEspecial"))