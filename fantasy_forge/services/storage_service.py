"""Data storage service."""

import json
import os
from typing import Optional, List
from pathlib import Path

from fantasy_forge.models.world import World
from fantasy_forge.models.character import Character
from fantasy_forge.models.manuscript import Manuscript


class StorageService:
    """Service for persisting and loading data."""

    def __init__(self, data_dir: str = "data"):
        """Initialize storage service.
        
        Args:
            data_dir: Directory for storing data files
        """
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.worlds_dir = self.data_dir / "worlds"
        self.characters_dir = self.data_dir / "characters"
        self.manuscripts_dir = self.data_dir / "manuscripts"
        
        self.worlds_dir.mkdir(exist_ok=True)
        self.characters_dir.mkdir(exist_ok=True)
        self.manuscripts_dir.mkdir(exist_ok=True)

    def save_world(self, world: World) -> bool:
        """Save world to file.
        
        Args:
            world: World object to save
            
        Returns:
            True if successful
        """
        try:
            filename = self._sanitize_filename(world.name) + ".json"
            filepath = self.worlds_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(world.to_dict(), f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error saving world: {e}")
            return False

    def load_world(self, name: str) -> Optional[World]:
        """Load world from file.
        
        Args:
            name: World name
            
        Returns:
            World object or None
        """
        try:
            filename = self._sanitize_filename(name) + ".json"
            filepath = self.worlds_dir / filename
            
            if not filepath.exists():
                return None
            
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return World.from_dict(data)
        except Exception as e:
            print(f"Error loading world: {e}")
            return None

    def list_worlds(self) -> List[str]:
        """List all saved worlds.
        
        Returns:
            List of world names
        """
        try:
            return [f.stem for f in self.worlds_dir.glob("*.json")]
        except:
            return []

    def save_character(self, character: Character) -> bool:
        """Save character to file.
        
        Args:
            character: Character object to save
            
        Returns:
            True if successful
        """
        try:
            filename = self._sanitize_filename(character.name) + ".json"
            filepath = self.characters_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(character.to_dict(), f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error saving character: {e}")
            return False

    def load_character(self, name: str) -> Optional[Character]:
        """Load character from file.
        
        Args:
            name: Character name
            
        Returns:
            Character object or None
        """
        try:
            filename = self._sanitize_filename(name) + ".json"
            filepath = self.characters_dir / filename
            
            if not filepath.exists():
                return None
            
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return Character.from_dict(data)
        except Exception as e:
            print(f"Error loading character: {e}")
            return None

    def list_characters(self) -> List[str]:
        """List all saved characters.
        
        Returns:
            List of character names
        """
        try:
            return [f.stem for f in self.characters_dir.glob("*.json")]
        except:
            return []

    def save_manuscript(self, manuscript: Manuscript) -> bool:
        """Save manuscript to file.
        
        Args:
            manuscript: Manuscript object to save
            
        Returns:
            True if successful
        """
        try:
            filename = self._sanitize_filename(manuscript.title) + ".json"
            filepath = self.manuscripts_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(manuscript.to_dict(), f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error saving manuscript: {e}")
            return False

    def load_manuscript(self, title: str) -> Optional[Manuscript]:
        """Load manuscript from file.
        
        Args:
            title: Manuscript title
            
        Returns:
            Manuscript object or None
        """
        try:
            filename = self._sanitize_filename(title) + ".json"
            filepath = self.manuscripts_dir / filename
            
            if not filepath.exists():
                return None
            
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return Manuscript.from_dict(data)
        except Exception as e:
            print(f"Error loading manuscript: {e}")
            return None

    def list_manuscripts(self) -> List[str]:
        """List all saved manuscripts.
        
        Returns:
            List of manuscript titles
        """
        try:
            return [f.stem for f in self.manuscripts_dir.glob("*.json")]
        except:
            return []

    def _sanitize_filename(self, name: str) -> str:
        """Sanitize name for use as filename.
        
        Args:
            name: Name to sanitize
            
        Returns:
            Safe filename
        """
        # Replace invalid characters
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            name = name.replace(char, '_')
        
        # Limit length
        return name[:100]
