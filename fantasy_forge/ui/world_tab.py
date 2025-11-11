"""World building tab."""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QLineEdit, QTextEdit, QListWidget, QSplitter, QGroupBox,
    QFormLayout, QMessageBox, QInputDialog
)
from PyQt6.QtCore import Qt

from fantasy_forge.models.world import World, Race, MagicSystem, Location, TimelineEvent
from fantasy_forge.services.storage_service import StorageService
from fantasy_forge.services.ollama_service import OllamaService


class WorldTab(QWidget):
    """World building tab."""

    def __init__(self, storage_service: StorageService, ollama_service: OllamaService):
        super().__init__()
        self.storage_service = storage_service
        self.ollama_service = ollama_service
        self.current_world = World(name="My Fantasy World", description="")
        self._setup_ui()

    def _setup_ui(self):
        """Setup UI components."""
        layout = QHBoxLayout()
        self.setLayout(layout)

        # Create splitter
        splitter = QSplitter(Qt.Orientation.Horizontal)
        layout.addWidget(splitter)

        # Left panel - World list and controls
        left_panel = self._create_left_panel()
        splitter.addWidget(left_panel)

        # Right panel - World details
        right_panel = self._create_right_panel()
        splitter.addWidget(right_panel)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 3)

    def _create_left_panel(self) -> QWidget:
        """Create left panel with world list."""
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        layout.addWidget(QLabel("<h3>Worlds</h3>"))

        # World list
        self.world_list = QListWidget()
        self.world_list.itemClicked.connect(self._load_selected_world)
        layout.addWidget(self.world_list)

        # Buttons
        btn_layout = QHBoxLayout()
        
        new_btn = QPushButton("New World")
        new_btn.clicked.connect(self._new_world)
        btn_layout.addWidget(new_btn)

        save_btn = QPushButton("Save World")
        save_btn.clicked.connect(self.save)
        btn_layout.addWidget(save_btn)

        layout.addLayout(btn_layout)

        # Load world list
        self._refresh_world_list()

        return panel

    def _create_right_panel(self) -> QWidget:
        """Create right panel with world details."""
        panel = QWidget()
        layout = QVBoxLayout()
        panel.setLayout(layout)

        # World info
        world_group = QGroupBox("World Information")
        world_layout = QFormLayout()
        world_group.setLayout(world_layout)

        self.name_input = QLineEdit()
        self.name_input.setText(self.current_world.name)
        world_layout.addRow("Name:", self.name_input)

        self.description_input = QTextEdit()
        self.description_input.setMaximumHeight(100)
        self.description_input.setText(self.current_world.description)
        world_layout.addRow("Description:", self.description_input)

        layout.addWidget(world_group)

        # Races section
        races_group = QGroupBox("Races")
        races_layout = QVBoxLayout()
        races_group.setLayout(races_layout)

        self.races_list = QListWidget()
        self.races_list.setMaximumHeight(150)
        races_layout.addWidget(self.races_list)

        races_btn_layout = QHBoxLayout()
        add_race_btn = QPushButton("Add Race")
        add_race_btn.clicked.connect(self._add_race)
        races_btn_layout.addWidget(add_race_btn)

        generate_race_btn = QPushButton("Generate Race (AI)")
        generate_race_btn.clicked.connect(self._generate_race)
        races_btn_layout.addWidget(generate_race_btn)

        races_layout.addLayout(races_btn_layout)
        layout.addWidget(races_group)

        # Magic Systems section
        magic_group = QGroupBox("Magic Systems")
        magic_layout = QVBoxLayout()
        magic_group.setLayout(magic_layout)

        self.magic_list = QListWidget()
        self.magic_list.setMaximumHeight(150)
        magic_layout.addWidget(self.magic_list)

        magic_btn_layout = QHBoxLayout()
        add_magic_btn = QPushButton("Add Magic System")
        add_magic_btn.clicked.connect(self._add_magic_system)
        magic_btn_layout.addWidget(add_magic_btn)

        generate_magic_btn = QPushButton("Generate Magic (AI)")
        generate_magic_btn.clicked.connect(self._generate_magic_system)
        magic_btn_layout.addWidget(generate_magic_btn)

        magic_layout.addLayout(magic_btn_layout)
        layout.addWidget(magic_group)

        # Locations section
        locations_group = QGroupBox("Locations")
        locations_layout = QVBoxLayout()
        locations_group.setLayout(locations_layout)

        self.locations_list = QListWidget()
        self.locations_list.setMaximumHeight(150)
        locations_layout.addWidget(self.locations_list)

        locations_btn_layout = QHBoxLayout()
        add_location_btn = QPushButton("Add Location")
        add_location_btn.clicked.connect(self._add_location)
        locations_btn_layout.addWidget(add_location_btn)

        generate_location_btn = QPushButton("Generate Location (AI)")
        generate_location_btn.clicked.connect(self._generate_location)
        locations_btn_layout.addWidget(generate_location_btn)

        locations_layout.addLayout(locations_btn_layout)
        layout.addWidget(locations_group)

        layout.addStretch()

        return panel

    def _refresh_world_list(self):
        """Refresh the world list."""
        self.world_list.clear()
        worlds = self.storage_service.list_worlds()
        self.world_list.addItems(worlds)

    def _load_selected_world(self):
        """Load the selected world."""
        current_item = self.world_list.currentItem()
        if current_item:
            world_name = current_item.text()
            world = self.storage_service.load_world(world_name)
            if world:
                self.current_world = world
                self._update_display()

    def _update_display(self):
        """Update display with current world data."""
        self.name_input.setText(self.current_world.name)
        self.description_input.setText(self.current_world.description)

        self.races_list.clear()
        for race in self.current_world.races:
            self.races_list.addItem(f"{race.name}: {race.description[:50]}...")

        self.magic_list.clear()
        for magic in self.current_world.magic_systems:
            self.magic_list.addItem(f"{magic.name}: {magic.description[:50]}...")

        self.locations_list.clear()
        for location in self.current_world.locations:
            self.locations_list.addItem(f"{location.name}: {location.description[:50]}...")

    def _new_world(self):
        """Create new world."""
        name, ok = QInputDialog.getText(self, "New World", "World name:")
        if ok and name:
            self.current_world = World(name=name, description="")
            self._update_display()

    def _add_race(self):
        """Add new race."""
        name, ok = QInputDialog.getText(self, "New Race", "Race name:")
        if ok and name:
            description, ok2 = QInputDialog.getText(self, "New Race", "Description:")
            if ok2:
                race = Race(name=name, description=description)
                self.current_world.races.append(race)
                self._update_display()

    def _generate_race(self):
        """Generate race using AI."""
        if not self.ollama_service.is_available():
            QMessageBox.warning(self, "AI Not Available", "Ollama is not running.")
            return

        result = self.ollama_service.generate_world_element("fantasy race")
        if result:
            # Parse result and create race
            lines = result.strip().split('\n')
            name = lines[0].replace("Name:", "").strip() if lines else "Generated Race"
            description = '\n'.join(lines[1:]) if len(lines) > 1 else result

            race = Race(name=name, description=description)
            self.current_world.races.append(race)
            self._update_display()

    def _add_magic_system(self):
        """Add new magic system."""
        name, ok = QInputDialog.getText(self, "New Magic System", "Magic system name:")
        if ok and name:
            description, ok2 = QInputDialog.getText(self, "New Magic System", "Description:")
            if ok2:
                magic = MagicSystem(name=name, description=description)
                self.current_world.magic_systems.append(magic)
                self._update_display()

    def _generate_magic_system(self):
        """Generate magic system using AI."""
        if not self.ollama_service.is_available():
            QMessageBox.warning(self, "AI Not Available", "Ollama is not running.")
            return

        result = self.ollama_service.generate_world_element("magic system")
        if result:
            lines = result.strip().split('\n')
            name = lines[0].replace("Name:", "").strip() if lines else "Generated Magic"
            description = '\n'.join(lines[1:]) if len(lines) > 1 else result

            magic = MagicSystem(name=name, description=description)
            self.current_world.magic_systems.append(magic)
            self._update_display()

    def _add_location(self):
        """Add new location."""
        name, ok = QInputDialog.getText(self, "New Location", "Location name:")
        if ok and name:
            description, ok2 = QInputDialog.getText(self, "New Location", "Description:")
            if ok2:
                location = Location(name=name, description=description)
                self.current_world.locations.append(location)
                self._update_display()

    def _generate_location(self):
        """Generate location using AI."""
        if not self.ollama_service.is_available():
            QMessageBox.warning(self, "AI Not Available", "Ollama is not running.")
            return

        name = self.ollama_service.generate_location_name("city")
        result = self.ollama_service.generate_world_element("fantasy location", f"for a place called {name}")
        
        if result:
            location = Location(name=name, description=result)
            self.current_world.locations.append(location)
            self._update_display()

    def save(self) -> bool:
        """Save current world."""
        self.current_world.name = self.name_input.text()
        self.current_world.description = self.description_input.toPlainText()

        if self.storage_service.save_world(self.current_world):
            self._refresh_world_list()
            return True
        return False

    def clear(self):
        """Clear current world."""
        self.current_world = World(name="My Fantasy World", description="")
        self._update_display()
