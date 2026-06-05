from utils.qtcore import *
from utils.config import *
from utils.path import *
from gui.styles.styles import getTheme, THEMES
from gui.widgets.custombuttons import NormalButton,SpecialButton

class UiMainWindow(object):

    def __init__(self, parent : QMainWindow):

        #/////// DEFININDO CONFIGURÇAÕES Á WINDOW ///////

        if not parent.objectName():
            parent.setObjectName("MainWindow") 

        parent.resize(*SIZE) # *(x,y) -> x, y
        parent.setMaximumSize(*SIZE)
        parent.setMinimumSize(*SIZE)

        self.theme = getTheme()

        #/////// CRIANDO E CONFIGURANDO QWIDGETS ///////

        # CENTRAL FRAME
        self.central_frame = QFrame()
        self.central_frame.setObjectName("central_frame")
        self.central_frame.setStyleSheet(""+self.theme.getStyleSheet("QFrame_Central"))
        self.central_frame_layout = QVBoxLayout(self.central_frame)

        # DISPLAY FRAME
        self.display_frame = QFrame()
        self.display_frame.setObjectName("display_frame")
        self.display_frame.setMinimumHeight(90)
        self.display_frame.setMaximumHeight(90)
        self.display_frame.setStyleSheet(""+self.theme.getStyleSheet("QDisplay_Frame"))
        self.display_frame_layout = QVBoxLayout(self.display_frame)

        self.display_label = QLabel()
        self.display_label.setMaximumHeight(60)
        self.display_label.setMinimumHeight(60)
        font_display_label = QFontDatabase.addApplicationFont((FONTS_DIR / "FiraCode-VariableFont_wght.ttf").as_posix())

        if font_display_label != -1:

            familias = QFontDatabase.applicationFontFamilies(font_display_label)
            fira_code_font = familias[0] if familias else "Arial"

            # 3. Cria a fonte customizada
            costumized_font = QFont(fira_code_font, 20) # Define o tamanho como 20
            self.display_label.setFont(costumized_font)
        
        self.display_label.setStyleSheet(self.theme.getStyleSheet("QDisplay_Label"))

        # BUTTONS' AREA FRAME
        self.btn_group_frame = QFrame()
        self.btn_group_frame.setObjectName("btn_group_frame")
        self.btn_group_frame.setStyleSheet(""+self.theme.getStyleSheet("QButton_Group_Frame"))
        self.btn_group_frame_layout = QHBoxLayout(self.btn_group_frame)
        self.btn_group_frame_layout.setContentsMargins(0,0,5,0)

        # BUTTONS
        btns_c_1 = QFrame()
        btns_c_1_layout = QVBoxLayout(btns_c_1)
        btns_c_2 = QFrame()
        btns_c_2_layout = QVBoxLayout(btns_c_2)
        btns_c_3 = QFrame()
        btns_c_3_layout = QVBoxLayout(btns_c_3)
        btns_c_4 = QFrame()
        btns_c_4_layout = QVBoxLayout(btns_c_4)

        self.btn_0 = NormalButton("0")
        self.btn_1 = NormalButton("1")
        self.btn_2 = NormalButton("2")
        self.btn_3 = NormalButton("3")
        self.btn_4 = NormalButton("4")
        self.btn_5 = NormalButton("5")
        self.btn_6 = NormalButton("6")
        self.btn_7 = NormalButton("7")
        self.btn_8 = NormalButton("8")
        self.btn_9 = NormalButton("9")

        self.btn_point = NormalButton(".")
        self.btn_equal = NormalButton("=")
        self.btn_plus = SpecialButton("+")
        self.btn_less = SpecialButton("-")
        self.btn_multi = SpecialButton("x")
        self.btn_division = SpecialButton("÷")

        self.btn_ac = SpecialButton("AC")
        self.btn_del = SpecialButton("DEL")
        self.btn_mod = SpecialButton("mod")
        self.btn_p = SpecialButton("( )")

        #/////// EXIBINDO QWIDGETS ///////

        # Colocando no display_frame
        self.display_frame_layout.addWidget(self.display_label)

        # Colocando no Central Frame
        self.central_frame_layout.addWidget(self.display_frame)
        self.central_frame_layout.addWidget(self.btn_group_frame)

        # Colocando os botões nas colunas
        btns_c_1_layout.addWidget(self.btn_mod)
        btns_c_1_layout.addWidget(self.btn_7)
        btns_c_1_layout.addWidget(self.btn_4)
        btns_c_1_layout.addWidget(self.btn_1)
        btns_c_1_layout.addWidget(self.btn_0)

        btns_c_2_layout.addWidget(self.btn_p)
        btns_c_2_layout.addWidget(self.btn_8)
        btns_c_2_layout.addWidget(self.btn_5)
        btns_c_2_layout.addWidget(self.btn_2)
        btns_c_2_layout.addWidget(self.btn_point)

        btns_c_3_layout.addWidget(self.btn_del)
        btns_c_3_layout.addWidget(self.btn_9)
        btns_c_3_layout.addWidget(self.btn_6)
        btns_c_3_layout.addWidget(self.btn_3)
        btns_c_3_layout.addWidget(self.btn_equal)

        btns_c_4_layout.addWidget(self.btn_ac)
        btns_c_4_layout.addWidget(self.btn_division)
        btns_c_4_layout.addWidget(self.btn_multi)
        btns_c_4_layout.addWidget(self.btn_less)
        btns_c_4_layout.addWidget(self.btn_plus)

        # Colocando no button group area
        self.btn_group_frame_layout.addWidget(btns_c_1)
        self.btn_group_frame_layout.addWidget(btns_c_2)
        self.btn_group_frame_layout.addWidget(btns_c_3)
        self.btn_group_frame_layout.addWidget(btns_c_4)

        # CONFIG FRAME
        self.config_frame = QFrame(self.central_frame)
        self.config_frame.setStyleSheet(self.theme.getStyleSheet("QConfig_Frame"))
        self.config_frame.resize(CONFIG_SIZE,SIZE[1])
        self.config_frame.move(-CONFIG_SIZE,0)
        self.config_frame_layout = QVBoxLayout(self.config_frame)

        self.themes_options = QComboBox()
        self.themes_options.addItems(list(THEMES.keys()))
        self.themes_options.setCurrentIndex(list(THEMES.keys()).index(style_list["actual_theme"]))
        self.themes_options.setStyleSheet(self.theme.getStyleSheet("QConfig_Options"))

        self.config_frame_layout.addWidget(self.themes_options)

        # Acoplando o frame central na janela
        parent.setCentralWidget(self.central_frame)

    def reload_ui(self): 
        """
        Recarrega todos os estilos
        """
        self.theme = getTheme()
        self.central_frame.setStyleSheet(""+self.theme.getStyleSheet("QFrame_Central"))
        self.btn_group_frame.setStyleSheet(""+self.theme.getStyleSheet("QButton_Group_Frame"))
        self.config_frame.setStyleSheet(self.theme.getStyleSheet("QConfig_Frame"))
        self.themes_options.setStyleSheet(self.theme.getStyleSheet("QConfig_Options"))

        self.central_frame.setStyleSheet(self.theme.getStyleSheet("QFrame_Central"))
        self.display_frame.setStyleSheet(self.theme.getStyleSheet("QDisplay_Frame"))
        self.display_label.setStyleSheet(self.theme.getStyleSheet("QDisplay_Label"))
        self.btn_group_frame.setStyleSheet(self.theme.getStyleSheet("QButton_Group_Frame"))

        self.btn_0.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_1.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_2.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_3.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_4.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_5.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_6.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_7.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_8.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_9.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_point.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))
        self.btn_equal.setStyleSheet(self.theme.getStyleSheet("QPushButtonNormal"))

        self.btn_plus.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))
        self.btn_less.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))
        self.btn_division.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))
        self.btn_multi.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))
        self.btn_ac.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))
        self.btn_mod.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))
        self.btn_p.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))
        self.btn_del.setStyleSheet(self.theme.getStyleSheet("QPushButtonEspecial"))