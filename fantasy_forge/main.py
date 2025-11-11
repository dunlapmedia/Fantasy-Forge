"""Main entry point for Fantasy Forge application."""

import sys
from PyQt6.QtWidgets import QApplication
from fantasy_forge.ui.main_window import MainWindow


def main():
    """Run the Fantasy Forge application."""
    app = QApplication(sys.argv)
    app.setApplicationName("Fantasy Forge")
    app.setOrganizationName("Fantasy Forge Team")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
