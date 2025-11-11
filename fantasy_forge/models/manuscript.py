"""Manuscript data models."""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Scene:
    """Scene model."""
    title: str
    content: str
    pov_character: str = ""
    location: str = ""
    notes: str = ""
    word_count: int = 0


@dataclass
class Chapter:
    """Chapter model."""
    number: int
    title: str
    synopsis: str = ""
    scenes: List[Scene] = field(default_factory=list)
    word_count: int = 0
    status: str = "draft"  # draft, revision, complete

    def calculate_word_count(self) -> int:
        """Calculate total word count for chapter."""
        total = 0
        for scene in self.scenes:
            total += len(scene.content.split())
        self.word_count = total
        return total


@dataclass
class PlotPoint:
    """Plot point model."""
    title: str
    description: str
    chapter: Optional[int] = None
    category: str = ""  # setup, inciting_incident, rising_action, climax, resolution


@dataclass
class Outline:
    """Story outline model."""
    title: str
    premise: str = ""
    plot_points: List[PlotPoint] = field(default_factory=list)
    character_arcs: Dict[str, str] = field(default_factory=dict)
    themes: List[str] = field(default_factory=list)
    notes: str = ""


@dataclass
class Manuscript:
    """Manuscript container."""
    title: str
    author: str = ""
    synopsis: str = ""
    genre: str = "Fantasy"
    outline: Optional[Outline] = None
    chapters: List[Chapter] = field(default_factory=list)
    word_count: int = 0
    target_word_count: int = 80000
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    modified_at: str = field(default_factory=lambda: datetime.now().isoformat())

    def calculate_word_count(self) -> int:
        """Calculate total word count for manuscript."""
        total = 0
        for chapter in self.chapters:
            total += chapter.calculate_word_count()
        self.word_count = total
        return total

    def to_dict(self) -> dict:
        """Convert manuscript to dictionary."""
        # Convert outline
        outline_dict = None
        if self.outline:
            outline_dict = {
                "title": self.outline.title,
                "premise": self.outline.premise,
                "plot_points": [vars(pp) for pp in self.outline.plot_points],
                "character_arcs": self.outline.character_arcs,
                "themes": self.outline.themes,
                "notes": self.outline.notes,
            }
        
        # Convert chapters
        chapters_dict = []
        for chapter in self.chapters:
            chapter_dict = {
                "number": chapter.number,
                "title": chapter.title,
                "synopsis": chapter.synopsis,
                "scenes": [vars(scene) for scene in chapter.scenes],
                "word_count": chapter.word_count,
                "status": chapter.status,
            }
            chapters_dict.append(chapter_dict)
        
        return {
            "title": self.title,
            "author": self.author,
            "synopsis": self.synopsis,
            "genre": self.genre,
            "outline": outline_dict,
            "chapters": chapters_dict,
            "word_count": self.word_count,
            "target_word_count": self.target_word_count,
            "created_at": self.created_at,
            "modified_at": self.modified_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Manuscript":
        """Create manuscript from dictionary."""
        manuscript = cls(
            title=data.get("title", ""),
            author=data.get("author", ""),
            synopsis=data.get("synopsis", ""),
            genre=data.get("genre", "Fantasy"),
            word_count=data.get("word_count", 0),
            target_word_count=data.get("target_word_count", 80000),
            created_at=data.get("created_at", datetime.now().isoformat()),
            modified_at=data.get("modified_at", datetime.now().isoformat()),
        )
        
        outline_data = data.get("outline")
        if outline_data:
            outline = Outline(
                title=outline_data.get("title", ""),
                premise=outline_data.get("premise", ""),
                themes=outline_data.get("themes", []),
                notes=outline_data.get("notes", ""),
                character_arcs=outline_data.get("character_arcs", {}),
            )
            for pp_data in outline_data.get("plot_points", []):
                outline.plot_points.append(PlotPoint(**pp_data))
            manuscript.outline = outline
        
        for chapter_data in data.get("chapters", []):
            chapter = Chapter(
                number=chapter_data.get("number", 0),
                title=chapter_data.get("title", ""),
                synopsis=chapter_data.get("synopsis", ""),
                word_count=chapter_data.get("word_count", 0),
                status=chapter_data.get("status", "draft"),
            )
            for scene_data in chapter_data.get("scenes", []):
                chapter.scenes.append(Scene(**scene_data))
            manuscript.chapters.append(chapter)
        
        return manuscript
