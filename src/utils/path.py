"""
    ARQUIVO PYTHON RESPONSÁVEL POR ARMAZENAR OS CAMINHOS DAS PASTAS DO SOFTWARE
"""

from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

ASSETS_DIR = BASE_DIR / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
ICONS_DIR = ASSETS_DIR / "icons"

GUI_DIR = BASE_DIR / "gui"
STYLES_DIR = GUI_DIR / "styles"
WIDGETS_DIR = GUI_DIR / "widgets"
WINDOWS_DIR = GUI_DIR / "windows"

APP_DIR = BASE_DIR / "app"
UTILS_DIR = BASE_DIR / "utils"