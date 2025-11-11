"""Character development tab."""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QTextEdit, QListWidget, QSplitter, QGroupBox,
    QFormLayout, QMessageBox, QInputDialog
)
from PyQt6.QtCore import Qt

from fantasy_forge.models.character import Character, CharacterRelationship
from fantasy_forge.services.storage_service import StorageService
from fantasy_forge.services.ollama_service import OllamaService


class CharacterTab(QWidget):
    """Character development tab."""

    def __init__(self, storage_service: StorageService, ollama_service: OllamaService):
        super().__init__()
        self.storage_service = storage_service
        self.ollama_service = ollama_service
        self.current_character = Character(name="New Character", description="")
        self._setup_ui()

    def _setup_ui(self):
        """Setup UI components."""
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Create splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)

        # Left panel - Character list
        left_panel = self._create_left_panel()
        splitter.addWidget(left_panel)

        # Right panel - Character details
        right_panel = self._create_right_panel()
        splitter.addWidget(right_panel)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 3)

    def _create_left_panel(self) -> QWidget:
        """Create left panel with character list."""
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        layout.addWidget(QLabel("<h3>Characters</h3>"))

        # Character list
        self.character_list = QListWidget()
        self.character_list.itemClicked.connect(self._load_selected_character)
        layout.addWidget(self.character_list)

        # Buttons
        btn_layout = QHBoxLayout()
        
        new_btn = QPushButton("New Character")
        new_btn.clicked.connect(self._new_character)
        btn_layout.addWidget(new_btn)

        save_btn = QPushButton("Save Character")
        save_btn.clicked.connect(self.save)
        btn_layout.addWidget(save_btn)

        layout.addLayout(btn_layout)

        # Generate name button
        generate_name_btn = QPushButton("Generate Name (AI)")
        generate_name_btn.clicked.connect(self._generate_name)
        layout.addWidget(generate_name_btn)

        # Load character list
        self._refresh_character_list()

        return panel

    def _create_right_panel(self) -> QWidget:
        """Create right panel with character details."""
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        # Basic info
        basic_group = QGroupBox("Basic Information")
        basic_layout = QFormLayout()
        basic_group.setLayout(basic_layout)

        self.name_input = QLineEdit()
        basic_layout.addRow("Name:", self.name_input)

        self.race_input = QLineEdit()
        basic_layout.addRow("Race:", self.race_input)

        self.age_input = QLineEdit()
        basic_layout.addRow("Age:", self.age_input)

        self.occupation_input = QLineEdit()
        basic_layout.addRow("Occupation:", self.occupation_input)

        layout.addWidget(basic_group)

        # Description and personality
        desc_group = QGroupBox("Description & Personality")
        desc_layout = QVBoxLayout()
        desc_group.setLayout(desc_layout)

        desc_layout.addWidget(QLabel("Description:"))
        self.description_input = QTextEdit()
        self.description_input.setMaximumHeight(80)
        desc_layout.addWidget(self.description_input)

        desc_layout.addWidget(QLabel("Appearance:"))
        self.appearance_input = QTextEdit()
        self.appearance_input.setMaximumHeight(80)
        desc_layout.addWidget(self.appearance_input)

        desc_layout.addWidget(QLabel("Personality:"))
        self.personality_input = QTextEdit()
        self.personality_input.setMaximumHeight(80)
        desc_layout.addWidget(self.personality_input)

        layout.addWidget(desc_group)

        # Backstory and arc
        story_group = QGroupBox("Story Elements")
        story_layout = QVBoxLayout()
        story_group.setLayout(story_layout)

        story_layout.addWidget(QLabel("Backstory:"))
        self.backstory_input = QTextEdit()
        self.backstory_input.setMaximumHeight(100)
        story_layout.addWidget(self.backstory_input)

        story_layout.addWidget(QLabel("Character Arc:"))
        self.arc_input = QTextEdit()
        self.arc_input.setMaximumHeight(80)
        story_layout.addWidget(self.arc_input)

        layout.addWidget(story_group)

        # Notes
        notes_group = QGroupBox("Notes")
        notes_layout = QVBoxLayout()
        notes_group.setLayout(notes_layout)

        self.notes_input = QTextEdit()
        self.notes_input.setMaximumHeight(100)
        notes_layout.addWidget(self.notes_input)

        layout.addWidget(notes_group)

        layout.addStretch()

        return panel

    def _refresh_character_list(self):
        """Refresh the character list."""
        self.character_list.clear()
        characters = self.storage_service.list_characters()
        self.character_list.addItems(characters)

    def _load_selected_character(self):
        """Load the selected character."""
        current_item = self.character_list.currentItem()
        if current_item:
            character_name = current_item.text()
            character = self.storage_service.load_character(character_name)
            if character:
                self.current_character = character
                self._update_display()

    def _update_display(self):
        """Update display with current character data."""
        self.name_input.setText(self.current_character.name)
        self.race_input.setText(self.current_character.race)
        self.age_input.setText(self.current_character.age)
        self.occupation_input.setText(self.current_character.occupation)
        self.description_input.setText(self.current_character.description)
        self.appearance_input.setText(self.current_character.appearance)
        self.personality_input.setText(self.current_character.personality)
        self.backstory_input.setText(self.current_character.backstory)
        self.arc_input.setText(self.current_character.arc)
        self.notes_input.setText(self.current_character.notes)

    def _new_character(self):
        """Create new character."""
        name, ok = QInputDialog.getText(self, "New Character", "Character name:")
        if ok and name:
            self.current_character = Character(name=name, description="")
            self._update_display()

    def _generate_name(self):
        """Generate character name using AI."""
        if not self.ollama_service.is_available():
            QMessageBox.warning(self, "AI Not Available", "Ollama is not running.")
            return

        race = self.race_input.text() or "human"
        name = self.ollama_service.generate_character_name(race)
        self.name_input.setText(name)

    def save(self) -> bool:
        """Save current character."""
        self.current_character.name = self.name_input.text()
        self.current_character.race = self.race_input.text()
        self.current_character.age = self.age_input.text()
        self.current_character.occupation = self.occupation_input.text()
        self.current_character.description = self.description_input.toPlainText()
        self.current_character.appearance = self.appearance_input.toPlainText()
        self.current_character.personality = self.personality_input.toPlainText()
        self.current_character.backstory = self.backstory_input.toPlainText()
        self.current_character.arc = self.arc_input.toPlainText()
        self.current_character.notes = self.notes_input.toPlainText()

        if self.storage_service.save_character(self.current_character):
            self._refresh_character_list()
            return True
        return False

    def clear(self):
        """Clear current character."""
        self.current_character = Character(name="New Character", description="")
        self._update_display()
