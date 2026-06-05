from utils.qtcore import *
from utils.config import *
from utils.path import *
from typing import Literal
import json


class ThemeStyle:
    """
    Classe padrão para temas da calculadora
    """

    def __init__(
            self,
            central_frame_background_color = "#3f3f3f",
            central_frame_background_highlight = "#4D4D4D",
            central_frame_background_border = "#292727",

            config_frame_background = "#e69028",

            display_frame_background = "#6e6a5b",
            display_frame_background_highlight = "#7c796e",
            display_frame_background_border = "#635e4b",

            display_label_background = "#dedede",
            display_label_background_shadow = "#c4c4c4",
            display_text_color = "#242424",

            btn_group_frame_background = "#5b626e",
            btn_group_frame_background_highlight = "#6e747e",
            btn_group_frame_background_border = "#464e5e",

            btn_frame_background = "#eda64e",
            btn_frame_background_border = "#e69028",
            btn_frame_background_hover = "#ec9c3b",
            btn_frame_background_click = "#eb942b",
            btn_text_color = "#242424",

            btn_e_frame_background = "#3A3A3A",
            btn_e_frame_background_border = "#242424",
            btn_e_frame_background_hover = "#2E2E2E",
            btn_e_frame_background_click = "#222222",
            btn_e_text_color = "#eda64e"

            ):
        
        self.central_frame_background_color = central_frame_background_color
        self.central_frame_background_highlight = central_frame_background_highlight
        self.central_frame_background_border = central_frame_background_border

        self.config_frame_background = config_frame_background 

        self.display_frame_background = display_frame_background
        self.display_frame_background_highlight = display_frame_background_highlight
        self.display_frame_background_border = display_frame_background_border

        self.display_label_background = display_label_background
        self.display_label_background_shadow = display_label_background_shadow
        self.display_text_color = display_text_color

        self.btn_group_frame_background = btn_group_frame_background
        self.btn_group_frame_background_highlight = btn_group_frame_background_highlight
        self.btn_group_frame_background_border = btn_group_frame_background_border

        self.btn_frame_background = btn_frame_background
        self.btn_text_color = btn_text_color
        self.btn_frame_background_border = btn_frame_background_border
        self.btn_frame_background_hover = btn_frame_background_hover
        self.btn_frame_background_click = btn_frame_background_click

        self.btn_e_frame_background = btn_e_frame_background
        self.btn_e_text_color = btn_e_text_color
        self.btn_e_frame_background_border = btn_e_frame_background_border
        self.btn_e_frame_background_hover = btn_e_frame_background_hover
        self.btn_e_frame_background_click = btn_e_frame_background_click

    def getStyleSheet(
        self,
        widget: Literal[
        "QPushButtonNormal",
        "QButton_Group_Frame",
        "QPushButtonEspecial",
        "QDisplay_Frame",
        "QDisplay_Label",
        "QFrame_Central",
        "QConfig_Frame",
        "QConfig_Options"
        ]) -> str:

        match widget:
            case "QPushButtonNormal":
                return f"""
                        QPushButton {{
                            background-color: {self.btn_frame_background};
                            border-top: none;
                            border-left: none;  
                            border-right: 5px solid {self.btn_frame_background_border};
                            border-bottom: 5px solid {self.btn_frame_background_border}; 
                            font-size: 15px;
                            font-weight: 600;
                            color: {self.btn_text_color};
                        }}
                        QPushButton:hover {{
                            background-color: {self.btn_frame_background_hover};
                        }}
                        QPushButton:pressed {{
                            background-color: {self.btn_frame_background_click};                           
                        }}
                    """
            case "QButton_Group_Frame":
                return f"""
                        #btn_group_frame {{
                            background-color: {self.btn_group_frame_background};
                            border-top: 6px solid {self.btn_group_frame_background_highlight}; 
                            border-left: 6px solid {self.btn_group_frame_background_highlight}; 
                            border-right: 6px solid {self.btn_group_frame_background_border}; 
                            border-bottom: 6px solid {self.btn_group_frame_background_border}; 
                        }}
                    """
            case "QPushButtonEspecial":
                return f"""
                        QPushButton {{
                            background-color: {self.btn_e_frame_background};
                            border-top: none;
                            border-left: none;  
                            border-right: 5px solid {self.btn_e_frame_background_border};
                            border-bottom: 5px solid {self.btn_e_frame_background_border}; 
                            font-size: 15px;
                            color: {self.btn_e_text_color};
                        }}
                        QPushButton:hover {{
                            background-color: {self.btn_e_frame_background_hover};
                        }}
                        QPushButton:pressed {{
                            background-color: {self.btn_e_frame_background_click};                           
                        }}
                    """            
            case "QDisplay_Frame":
                return f"""
                        #display_frame {{
                            background-color: {self.display_frame_background};                       
                            border-top: 5px solid {self.display_frame_background_highlight}; 
                            border-left: 5px solid {self.display_frame_background_highlight}; 
                            border-right: 5px solid {self.display_frame_background_border}; 
                            border-bottom: 5px solid {self.display_frame_background_border}; 
                        }}
                    """
            case "QDisplay_Label":
                return f"""
                        QLabel {{
                            background-color: {self.display_label_background};                        
                            border-top: 5px solid {self.display_label_background_shadow}; 
                            border-left: 5px solid {self.display_label_background_shadow}; 
                            color: {self.display_text_color};
                            font-weight: 600;
                        }}
                    """
            case "QFrame_Central":
                return f"""
                        #central_frame {{
                            background-color: {self.central_frame_background_color};                        
                            border-top: 6px solid {self.central_frame_background_highlight}; 
                            border-left: 6px solid {self.central_frame_background_highlight}; 
                            border-right: 6px solid {self.central_frame_background_border}; 
                            border-bottom: 6px solid {self.central_frame_background_border}; 
                        }}
                    """
            case "QConfig_Frame":
                return f"""
                        background-color: {self.config_frame_background};                        
                    """                
            case "QConfig_Options":
                return f"""
                        background-color: {self.display_label_background};                        
                        color: {self.display_text_color};
                        padding: 10px                        
                    """                
            case _:
                print("[!] Estilo não encontrado!")
                return ""
            
THEMES = {
}

style_list = {}

with open(STYLES_DIR / "styles.json", "r", encoding="utf-8") as json_file:
    style_list = json.load(json_file)

for style_name, value in style_list["themes"].items():

    THEMES[style_name] = ThemeStyle(**value)

def getTheme() -> ThemeStyle:
    return THEMES[style_list["actual_theme"]]

def reload_theme(theme_name : str) -> None:

    with open(STYLES_DIR / "styles.json", "w", encoding="utf-8") as json_file:
        style_list["actual_theme"] = theme_name
        json.dump(style_list,json_file,indent=4)