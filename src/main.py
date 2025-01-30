import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from nicegui import ui
from src.ui.interface import configure_ui

def main():
    configure_ui() 
    
    ui.run(
        host='0.0.0.0',
        port=7001,
        title='Aquatic Coastal Analysis',
        reload=True,
    )

if __name__ in {"__main__", "__mp_main__"}:
    main()