"""Main application window."""

from PyQt6.QtWidgets import (
    QMainWindow, QTabWidget, QWidget, QVBoxLayout, QHBoxLayout,
    QMenuBar, QMenu, QStatusBar, QMessageBox, QApplication
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

from fantasy_forge.ui.world_tab import WorldTab
from fantasy_forge.ui.character_tab import CharacterTab
from fantasy_forge.ui.manuscript_tab import ManuscriptTab
from fantasy_forge.ui.tools_tab import ToolsTab
from fantasy_forge.services.storage_service import StorageService
from fantasy_forge.services.ollama_service import OllamaService


class MainWindow(QMainWindow):
    """Main application window."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fantasy Forge - Fantasy Fiction Writing Tool")
        self.setGeometry(100, 100, 1400, 900)

        # Initialize services
        self.storage_service = StorageService()
        self.ollama_service = OllamaService()

        # Check Ollama availability
        self.ollama_available = self.ollama_service.is_available()

        # Setup UI
        self._setup_menu_bar()
        self._setup_central_widget()
        self._setup_status_bar()

        # Apply default theme
        self.dark_mode = False
        self._apply_theme()

    def _setup_menu_bar(self):
        """Setup menu bar."""
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu("&File")

        new_action = QAction("&New Project", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._new_project)
        file_menu.addAction(new_action)

        open_action = QAction("&Open Project", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self._open_project)
        file_menu.addAction(open_action)

        save_action = QAction("&Save", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self._save_project)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # View menu
        view_menu = menubar.addMenu("&View")

        theme_action = QAction("Toggle &Dark Mode", self)
        theme_action.setShortcut("Ctrl+D")
        theme_action.triggered.connect(self._toggle_theme)
        view_menu.addAction(theme_action)

        # Help menu
        help_menu = menubar.addMenu("&Help")

        about_action = QAction("&About", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)

        ollama_status_action = QAction("Ollama &Status", self)
        ollama_status_action.triggered.connect(self._show_ollama_status)
        help_menu.addAction(ollama_status_action)

    def _setup_central_widget(self):
        """Setup central widget with tabs."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create tab widget
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # Create tabs
        self.world_tab = WorldTab(self.storage_service, self.ollama_service)
        self.character_tab = CharacterTab(self.storage_service, self.ollama_service)
        self.manuscript_tab = ManuscriptTab(self.storage_service, self.ollama_service)
        self.tools_tab = ToolsTab(self.ollama_service)

        self.tabs.addTab(self.manuscript_tab, "📝 Manuscript")
        self.tabs.addTab(self.world_tab, "🌍 World Building")
        self.tabs.addTab(self.character_tab, "👤 Characters")
        self.tabs.addTab(self.tools_tab, "🛠️ Tools")

    def _setup_status_bar(self):
        """Setup status bar."""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        status_text = "Ready"
        if self.ollama_available:
            status_text += " | Ollama: Connected"
        else:
            status_text += " | Ollama: Not Available"

        self.status_bar.showMessage(status_text)

    def _toggle_theme(self):
        """Toggle between dark and light theme."""
        self.dark_mode = not self.dark_mode
        self._apply_theme()

    def _apply_theme(self):
        """Apply theme to application."""
        if self.dark_mode:
            # Dark theme
            dark_stylesheet = """
                QMainWindow, QWidget {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QTextEdit, QLineEdit, QPlainTextEdit, QListWidget, QTableWidget {
                    background-color: #1e1e1e;
                    color: #ffffff;
                    border: 1px solid #555555;
                }
                QPushButton {
                    background-color: #0d7377;
                    color: #ffffff;
                    border: none;
                    padding: 5px 15px;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #14a2a8;
                }
                QTabWidget::pane {
                    border: 1px solid #555555;
                }
                QTabBar::tab {
                    background-color: #3c3c3c;
                    color: #ffffff;
                    padding: 8px 16px;
                    border: 1px solid #555555;
                }
                QTabBar::tab:selected {
                    background-color: #0d7377;
                }
                QMenuBar {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QMenuBar::item:selected {
                    background-color: #0d7377;
                }
                QMenu {
                    background-color: #2b2b2b;
                    color: #ffffff;
                }
                QMenu::item:selected {
                    background-color: #0d7377;
                }
            """
            self.setStyleSheet(dark_stylesheet)
        else:
            # Light theme (default)
            self.setStyleSheet("")

    def _new_project(self):
        """Create new project."""
        reply = QMessageBox.question(
            self,
            "New Project",
            "Create a new project? Any unsaved changes will be lost.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            self.world_tab.clear()
            self.character_tab.clear()
            self.manuscript_tab.clear()
            self.status_bar.showMessage("New project created")

    def _open_project(self):
        """Open existing project."""
        self.status_bar.showMessage("Open project not yet implemented")

    def _save_project(self):
        """Save current project."""
        success = True
        success &= self.world_tab.save()
        success &= self.character_tab.save()
        success &= self.manuscript_tab.save()

        if success:
            self.status_bar.showMessage("Project saved successfully")
        else:
            self.status_bar.showMessage("Error saving project")

    def _show_about(self):
        """Show about dialog."""
        QMessageBox.about(
            self,
            "About Fantasy Forge",
            "<h2>Fantasy Forge</h2>"
            "<p>Version 0.1.0</p>"
            "<p>A multifeatured application for fantasy fiction writers, "
            "providing tools for worldbuilding, character development, "
            "and manuscript writing.</p>"
            "<p><b>Features:</b></p>"
            "<ul>"
            "<li>Worldbuilding tools (races, magic systems, locations, timelines)</li>"
            "<li>Character profile builder</li>"
            "<li>Manuscript drafting and tracking</li>"
            "<li>AI-powered writing assistance (via Ollama)</li>"
            "<li>Text analysis and editing tools</li>"
            "</ul>"
        )

    def _show_ollama_status(self):
        """Show Ollama connection status."""
        if self.ollama_available:
            QMessageBox.information(
                self,
                "Ollama Status",
                "<p><b>Status:</b> Connected</p>"
                "<p>Ollama is running and available for AI-powered features.</p>"
            )
        else:
            QMessageBox.warning(
                self,
                "Ollama Status",
                "<p><b>Status:</b> Not Available</p>"
                "<p>Ollama is not running or not accessible at http://localhost:11434</p>"
                "<p>AI-powered features will not be available.</p>"
                "<p>To use AI features, please install and start Ollama.</p>"
            )

    def closeEvent(self, event):
        """Handle window close event."""
        reply = QMessageBox.question(
            self,
            "Exit Fantasy Forge",
            "Are you sure you want to exit? Make sure to save your work.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
