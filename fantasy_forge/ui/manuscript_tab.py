"""Manuscript writing tab."""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QTextEdit, QListWidget, QSplitter, QGroupBox,
    QFormLayout, QMessageBox, QInputDialog, QProgressBar
)
from PyQt6.QtCore import Qt

from fantasy_forge.models.manuscript import Manuscript, Chapter, Scene, Outline, PlotPoint
from fantasy_forge.services.storage_service import StorageService
from fantasy_forge.services.ollama_service import OllamaService


class ManuscriptTab(QWidget):
    """Manuscript writing tab."""

    def __init__(self, storage_service: StorageService, ollama_service: OllamaService):
        super().__init__()
        self.storage_service = storage_service
        self.ollama_service = ollama_service
        self.current_manuscript = Manuscript(title="My Novel")
        self.current_chapter = None
        self._setup_ui()

    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Manuscript info section
        info_group = QGroupBox("Manuscript Information")
        info_layout = QFormLayout()
        info_group.setLayout(info_layout)

        self.title_input = QLineEdit()
        self.title_input.setText(self.current_manuscript.title)
        info_layout.addRow("Title:", self.title_input)

        self.author_input = QLineEdit()
        self.author_input.setText(self.current_manuscript.author)
        info_layout.addRow("Author:", self.author_input)

        self.synopsis_input = QTextEdit()
        self.synopsis_input.setMaximumHeight(80)
        self.synopsis_input.setText(self.current_manuscript.synopsis)
        info_layout.addRow("Synopsis:", self.synopsis_input)

        layout.addWidget(info_group)

        # Progress section
        progress_group = QGroupBox("Progress")
        progress_layout = QVBoxLayout()
        progress_group.setLayout(progress_layout)

        self.progress_label = QLabel("Word Count: 0 / 80,000 (0%)")
        progress_layout.addWidget(self.progress_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)

        layout.addWidget(progress_group)

        # Main content area
        content_splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(content_splitter)

        # Left: Chapter list
        left_panel = self._create_left_panel()
        content_splitter.addWidget(left_panel)

        # Right: Chapter editor
        right_panel = self._create_right_panel()
        content_splitter.addWidget(right_panel)

        content_splitter.setStretchFactor(0, 1)
        content_splitter.setStretchFactor(1, 3)

        # Buttons
        btn_layout = QHBoxLayout()
        
        load_btn = QPushButton("Load Manuscript")
        load_btn.clicked.connect(self._load_manuscript)
        btn_layout.addWidget(load_btn)

        save_btn = QPushButton("Save Manuscript")
        save_btn.clicked.connect(self.save)
        btn_layout.addWidget(save_btn)

        prompt_btn = QPushButton("Get Writing Prompt (AI)")
        prompt_btn.clicked.connect(self._get_writing_prompt)
        btn_layout.addWidget(prompt_btn)

        layout.addLayout(btn_layout)

    def _create_left_panel(self) -> QWidget:
        """Create left panel with chapter list."""
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        layout.addWidget(QLabel("<h3>Chapters</h3>"))

        # Chapter list
        self.chapter_list = QListWidget()
        self.chapter_list.itemClicked.connect(self._load_selected_chapter)
        layout.addWidget(self.chapter_list)

        # Chapter buttons
        chapter_btn_layout = QHBoxLayout()
        
        add_chapter_btn = QPushButton("Add Chapter")
        add_chapter_btn.clicked.connect(self._add_chapter)
        chapter_btn_layout.addWidget(add_chapter_btn)

        delete_chapter_btn = QPushButton("Delete Chapter")
        delete_chapter_btn.clicked.connect(self._delete_chapter)
        chapter_btn_layout.addWidget(delete_chapter_btn)

        layout.addLayout(chapter_btn_layout)

        return panel

    def _create_right_panel(self) -> QWidget:
        """Create right panel with chapter editor."""
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        # Chapter info
        chapter_info_layout = QHBoxLayout()
        
        chapter_info_layout.addWidget(QLabel("Chapter Title:"))
        self.chapter_title_input = QLineEdit()
        chapter_info_layout.addWidget(self.chapter_title_input)

        self.chapter_status_label = QLabel("Status: Not Selected")
        chapter_info_layout.addWidget(self.chapter_status_label)

        layout.addLayout(chapter_info_layout)

        # Chapter synopsis
        layout.addWidget(QLabel("Synopsis:"))
        self.chapter_synopsis_input = QTextEdit()
        self.chapter_synopsis_input.setMaximumHeight(60)
        layout.addWidget(self.chapter_synopsis_input)

        # Chapter content
        layout.addWidget(QLabel("Content:"))
        self.chapter_content_input = QTextEdit()
        layout.addWidget(self.chapter_content_input)

        # Update chapter button
        update_btn = QPushButton("Update Chapter")
        update_btn.clicked.connect(self._update_chapter)
        layout.addWidget(update_btn)

        return panel

    def _add_chapter(self):
        """Add new chapter."""
        chapter_num = len(self.current_manuscript.chapters) + 1
        title, ok = QInputDialog.getText(
            self, "New Chapter", f"Chapter {chapter_num} title:",
            text=f"Chapter {chapter_num}"
        )
        
        if ok:
            chapter = Chapter(number=chapter_num, title=title)
            chapter.scenes.append(Scene(title="Scene 1", content=""))
            self.current_manuscript.chapters.append(chapter)
            self._refresh_chapter_list()

    def _delete_chapter(self):
        """Delete selected chapter."""
        if self.current_chapter:
            reply = QMessageBox.question(
                self, "Delete Chapter",
                f"Delete {self.current_chapter.title}?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            
            if reply == QMessageBox.StandardButton.Yes:
                self.current_manuscript.chapters.remove(self.current_chapter)
                self.current_chapter = None
                self._refresh_chapter_list()
                self._clear_chapter_editor()

    def _load_selected_chapter(self):
        """Load selected chapter for editing."""
        current_item = self.chapter_list.currentItem()
        if current_item:
            chapter_index = self.chapter_list.currentRow()
            if 0 <= chapter_index < len(self.current_manuscript.chapters):
                self.current_chapter = self.current_manuscript.chapters[chapter_index]
                self._update_chapter_display()

    def _update_chapter_display(self):
        """Update chapter editor with current chapter data."""
        if self.current_chapter:
            self.chapter_title_input.setText(self.current_chapter.title)
            self.chapter_synopsis_input.setText(self.current_chapter.synopsis)
            
            # Combine all scene content
            content = ""
            for scene in self.current_chapter.scenes:
                if scene.title:
                    content += f"## {scene.title}\n\n"
                content += scene.content + "\n\n"
            
            self.chapter_content_input.setText(content)
            self.chapter_status_label.setText(f"Status: {self.current_chapter.status}")

    def _clear_chapter_editor(self):
        """Clear chapter editor."""
        self.chapter_title_input.clear()
        self.chapter_synopsis_input.clear()
        self.chapter_content_input.clear()
        self.chapter_status_label.setText("Status: Not Selected")

    def _update_chapter(self):
        """Update current chapter with editor content."""
        if self.current_chapter:
            self.current_chapter.title = self.chapter_title_input.text()
            self.current_chapter.synopsis = self.chapter_synopsis_input.toPlainText()
            
            # Update first scene with content (simplified)
            content = self.chapter_content_input.toPlainText()
            if self.current_chapter.scenes:
                self.current_chapter.scenes[0].content = content
            
            self.current_chapter.calculate_word_count()
            self._refresh_chapter_list()
            self._update_progress()
            
            QMessageBox.information(self, "Success", "Chapter updated successfully!")

    def _refresh_chapter_list(self):
        """Refresh chapter list."""
        self.chapter_list.clear()
        for chapter in self.current_manuscript.chapters:
            self.chapter_list.addItem(
                f"{chapter.number}. {chapter.title} ({chapter.word_count} words)"
            )

    def _update_progress(self):
        """Update progress display."""
        word_count = self.current_manuscript.calculate_word_count()
        target = self.current_manuscript.target_word_count
        percentage = int((word_count / target) * 100) if target > 0 else 0
        
        self.progress_label.setText(f"Word Count: {word_count:,} / {target:,} ({percentage}%)")
        self.progress_bar.setValue(min(percentage, 100))

    def _load_manuscript(self):
        """Load manuscript from storage."""
        manuscripts = self.storage_service.list_manuscripts()
        if not manuscripts:
            QMessageBox.information(self, "No Manuscripts", "No saved manuscripts found.")
            return
        
        title, ok = QInputDialog.getItem(
            self, "Load Manuscript", "Select manuscript:",
            manuscripts, 0, False
        )
        
        if ok and title:
            manuscript = self.storage_service.load_manuscript(title)
            if manuscript:
                self.current_manuscript = manuscript
                self.title_input.setText(self.current_manuscript.title)
                self.author_input.setText(self.current_manuscript.author)
                self.synopsis_input.setText(self.current_manuscript.synopsis)
                self._refresh_chapter_list()
                self._update_progress()

    def _get_writing_prompt(self):
        """Get writing prompt from AI."""
        if not self.ollama_service.is_available():
            QMessageBox.warning(self, "AI Not Available", "Ollama is not running.")
            return

        prompt = self.ollama_service.generate_writing_prompt("fantasy")
        QMessageBox.information(self, "Writing Prompt", prompt)

    def save(self) -> bool:
        """Save current manuscript."""
        self.current_manuscript.title = self.title_input.text()
        self.current_manuscript.author = self.author_input.text()
        self.current_manuscript.synopsis = self.synopsis_input.toPlainText()

        if self.storage_service.save_manuscript(self.current_manuscript):
            QMessageBox.information(self, "Success", "Manuscript saved successfully!")
            return True
        else:
            QMessageBox.warning(self, "Error", "Failed to save manuscript.")
            return False

    def clear(self):
        """Clear current manuscript."""
        self.current_manuscript = Manuscript(title="My Novel")
        self.current_chapter = None
        self.title_input.setText(self.current_manuscript.title)
        self.author_input.clear()
        self.synopsis_input.clear()
        self._refresh_chapter_list()
        self._clear_chapter_editor()
        self._update_progress()
