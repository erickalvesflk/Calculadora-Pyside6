"""
Armazena as constantes configuráveis do software
"""
from utils.path import *
import json
style_list = {}

with open(STYLES_DIR / "styles.json", "r", encoding="utf-8") as json_file:
    style_list = json.load(json_file)

THEME = style_list["actual_theme"] # Pode ser default, ...
SIZE = (300,450)
CONFIG_SIZE = 120
