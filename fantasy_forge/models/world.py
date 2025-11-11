"""World building data models."""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
import json


@dataclass
class Race:
    """Fantasy race model."""
    name: str
    description: str
    traits: List[str] = field(default_factory=list)
    culture: str = ""
    lifespan: str = ""
    appearance: str = ""


@dataclass
class MagicSystem:
    """Magic system model."""
    name: str
    description: str
    rules: List[str] = field(default_factory=list)
    limitations: List[str] = field(default_factory=list)
    source: str = ""


@dataclass
class Location:
    """Geographic location model."""
    name: str
    description: str
    geography: str = ""
    climate: str = ""
    population: str = ""
    notable_features: List[str] = field(default_factory=list)
    coordinates: Optional[tuple] = None


@dataclass
class TimelineEvent:
    """Timeline event model."""
    title: str
    description: str
    date: str
    category: str = ""
    related_characters: List[str] = field(default_factory=list)
    related_locations: List[str] = field(default_factory=list)


@dataclass
class World:
    """Fantasy world container."""
    name: str
    description: str
    races: List[Race] = field(default_factory=list)
    magic_systems: List[MagicSystem] = field(default_factory=list)
    locations: List[Location] = field(default_factory=list)
    timeline: List[TimelineEvent] = field(default_factory=list)
    cultures: Dict[str, str] = field(default_factory=dict)
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    modified_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def to_dict(self) -> dict:
        """Convert world to dictionary."""
        return {
            "name": self.name,
            "description": self.description,
            "races": [vars(r) for r in self.races],
            "magic_systems": [vars(m) for m in self.magic_systems],
            "locations": [vars(l) for l in self.locations],
            "timeline": [vars(e) for e in self.timeline],
            "cultures": self.cultures,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "World":
        """Create world from dictionary."""
        world = cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            cultures=data.get("cultures", {}),
            created_at=data.get("created_at", datetime.now().isoformat()),
            modified_at=data.get("modified_at", datetime.now().isoformat()),
        )
        
        for race_data in data.get("races", []):
            world.races.append(Race(**race_data))
        
        for magic_data in data.get("magic_systems", []):
            world.magic_systems.append(MagicSystem(**magic_data))
        
        for loc_data in data.get("locations", []):
            world.locations.append(Location(**loc_data))
        
        for event_data in data.get("timeline", []):
            world.timeline.append(TimelineEvent(**event_data))
        
        return world
