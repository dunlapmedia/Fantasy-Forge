"""Character data models."""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class CharacterRelationship:
    """Character relationship model."""
    character_name: str
    relationship_type: str
    description: str = ""


@dataclass
class Character:
    """Character profile model."""
    name: str
    description: str
    backstory: str = ""
    personality: str = ""
    traits: List[str] = field(default_factory=list)
    goals: List[str] = field(default_factory=list)
    fears: List[str] = field(default_factory=list)
    relationships: List[CharacterRelationship] = field(default_factory=list)
    appearance: str = ""
    age: str = ""
    race: str = ""
    occupation: str = ""
    skills: List[str] = field(default_factory=list)
    arc: str = ""
    notes: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    modified_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        """Convert character to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "backstory": self.backstory,
            "personality": self.personality,
            "traits": self.traits,
            "goals": self.goals,
            "fears": self.fears,
            "relationships": [vars(r) for r in self.relationships],
            "appearance": self.appearance,
            "age": self.age,
            "race": self.race,
            "occupation": self.occupation,
            "skills": self.skills,
            "arc": self.arc,
            "notes": self.notes,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Character":
        """Create character from dictionary."""
        character = cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            backstory=data.get("backstory", ""),
            personality=data.get("personality", ""),
            traits=data.get("traits", []),
            goals=data.get("goals", []),
            fears=data.get("fears", []),
            appearance=data.get("appearance", ""),
            age=data.get("age", ""),
            race=data.get("race", ""),
            occupation=data.get("occupation", ""),
            skills=data.get("skills", []),
            arc=data.get("arc", ""),
            notes=data.get("notes", ""),
            created_at=data.get("created_at", datetime.now().isoformat()),
            modified_at=data.get("modified_at", datetime.now().isoformat()),
        )
        
        for rel_data in data.get("relationships", []):
            character.relationships.append(CharacterRelationship(**rel_data))
        
        return character
