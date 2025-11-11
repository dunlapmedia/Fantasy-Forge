#!/usr/bin/env python3
"""Test script to verify Fantasy Forge functionality."""

import sys
import tempfile
import shutil
from pathlib import Path

# Test imports
print("=" * 60)
print("Fantasy Forge - Functionality Test")
print("=" * 60)
print()

print("1. Testing imports...")
try:
    from fantasy_forge.models.world import World, Race, MagicSystem, Location, TimelineEvent
    from fantasy_forge.models.character import Character, CharacterRelationship
    from fantasy_forge.models.manuscript import Manuscript, Chapter, Scene, Outline, PlotPoint
    from fantasy_forge.services.storage_service import StorageService
    from fantasy_forge.services.ollama_service import OllamaService
    from fantasy_forge.utils.text_analysis import TextAnalyzer
    print("   ✓ All imports successful")
except Exception as e:
    print(f"   ✗ Import failed: {e}")
    sys.exit(1)

# Test data models
print("\n2. Testing data models...")
try:
    # World model
    world = World(name="Aethoria", description="A magical realm")
    world.races.append(Race(name="Eldar", description="Ancient immortals", traits=["wise", "magical"]))
    world.magic_systems.append(MagicSystem(name="Runecasting", description="Magic through runes"))
    world.locations.append(Location(name="Crystal Peaks", description="Mystical mountains"))
    world.timeline.append(TimelineEvent(title="The Awakening", description="Magic returns", date="Year 0"))
    print("   ✓ World model works")
    
    # Character model
    character = Character(name="Lyra Stormwind", description="Elven mage")
    character.race = "Eldar"
    character.personality = "Curious and brave"
    character.backstory = "Born in the Crystal Peaks during a storm"
    character.relationships.append(
        CharacterRelationship(character_name="Theron", relationship_type="mentor", description="Her teacher")
    )
    print("   ✓ Character model works")
    
    # Manuscript model
    manuscript = Manuscript(title="The Chronicles of Aethoria", author="Fantasy Writer")
    manuscript.synopsis = "An epic tale of magic and adventure"
    
    chapter1 = Chapter(number=1, title="The Beginning")
    scene1 = Scene(title="Opening Scene", content="The storm raged over the Crystal Peaks...")
    chapter1.scenes.append(scene1)
    manuscript.chapters.append(chapter1)
    
    word_count = manuscript.calculate_word_count()
    print(f"   ✓ Manuscript model works (Word count: {word_count})")
    
except Exception as e:
    print(f"   ✗ Data model test failed: {e}")
    sys.exit(1)

# Test storage service
print("\n3. Testing storage service...")
temp_dir = tempfile.mkdtemp()
try:
    storage = StorageService(temp_dir)
    
    # Save and load world
    assert storage.save_world(world), "Failed to save world"
    loaded_world = storage.load_world("Aethoria")
    assert loaded_world is not None, "Failed to load world"
    assert loaded_world.name == "Aethoria", "World data mismatch"
    assert len(loaded_world.races) == 1, "World race count mismatch"
    print("   ✓ World storage/loading works")
    
    # Save and load character
    assert storage.save_character(character), "Failed to save character"
    loaded_char = storage.load_character("Lyra Stormwind")
    assert loaded_char is not None, "Failed to load character"
    assert loaded_char.name == "Lyra Stormwind", "Character data mismatch"
    print("   ✓ Character storage/loading works")
    
    # Save and load manuscript
    assert storage.save_manuscript(manuscript), "Failed to save manuscript"
    loaded_ms = storage.load_manuscript("The Chronicles of Aethoria")
    assert loaded_ms is not None, "Failed to load manuscript"
    assert loaded_ms.title == "The Chronicles of Aethoria", "Manuscript data mismatch"
    assert len(loaded_ms.chapters) == 1, "Manuscript chapter count mismatch"
    print("   ✓ Manuscript storage/loading works")
    
    # Test list functions
    worlds = storage.list_worlds()
    characters = storage.list_characters()
    manuscripts = storage.list_manuscripts()
    print(f"   ✓ List functions work ({len(worlds)} worlds, {len(characters)} characters, {len(manuscripts)} manuscripts)")
    
except Exception as e:
    print(f"   ✗ Storage test failed: {e}")
    sys.exit(1)
finally:
    shutil.rmtree(temp_dir)

# Test text analysis
print("\n4. Testing text analysis...")
try:
    analyzer = TextAnalyzer()
    
    test_text = """
    The wizard walked through the forest. The wizard was very powerful and wise.
    The ancient forest was dark and mysterious. He walked slowly through the dense path.
    The path was narrow and winding. Magic filled the air around the wizard.
    """
    
    # Word count
    word_count = analyzer.count_words(test_text)
    print(f"   ✓ Word count: {word_count} words")
    
    # Repeated words
    repeated = analyzer.find_repeated_words(test_text, min_count=2)
    print(f"   ✓ Repetition detection: {len(repeated)} repeated words found")
    
    # Repeated phrases
    phrases = analyzer.find_repeated_phrases(test_text, min_count=2)
    print(f"   ✓ Phrase detection: {len(phrases)} repeated phrases found")
    
    # Readability
    readability = analyzer.calculate_readability_score(test_text)
    print(f"   ✓ Readability: {readability['avg_sentence_length']:.1f} words/sentence")
    
    # Passive voice
    passive_text = "The spell was cast by the wizard. The door was opened."
    passive = analyzer.detect_passive_voice(passive_text)
    print(f"   ✓ Passive voice detection: {len(passive)} instances found")
    
    # Character name extraction
    names = analyzer.extract_character_names(test_text)
    print(f"   ✓ Name extraction: {len(names)} potential names found")
    
except Exception as e:
    print(f"   ✗ Text analysis test failed: {e}")
    sys.exit(1)

# Test Ollama service
print("\n5. Testing Ollama service...")
try:
    ollama = OllamaService()
    available = ollama.is_available()
    
    if available:
        print("   ✓ Ollama is running and available")
        print("   ℹ AI features will be fully functional")
    else:
        print("   ✓ Ollama service handles unavailability gracefully")
        print("   ℹ AI features will be disabled (expected in CI/test environments)")
    
except Exception as e:
    print(f"   ✗ Ollama service test failed: {e}")
    sys.exit(1)

# Test serialization roundtrip
print("\n6. Testing data serialization...")
try:
    # World
    world_dict = world.to_dict()
    world_restored = World.from_dict(world_dict)
    assert world_restored.name == world.name, "World serialization failed"
    print("   ✓ World serialization roundtrip works")
    
    # Character
    char_dict = character.to_dict()
    char_restored = Character.from_dict(char_dict)
    assert char_restored.name == character.name, "Character serialization failed"
    print("   ✓ Character serialization roundtrip works")
    
    # Manuscript
    ms_dict = manuscript.to_dict()
    ms_restored = Manuscript.from_dict(ms_dict)
    assert ms_restored.title == manuscript.title, "Manuscript serialization failed"
    print("   ✓ Manuscript serialization roundtrip works")
    
except Exception as e:
    print(f"   ✗ Serialization test failed: {e}")
    sys.exit(1)

# Summary
print("\n" + "=" * 60)
print("✓ ALL TESTS PASSED!")
print("=" * 60)
print("\nFantasy Forge core functionality is working correctly.")
print("\nTo run the application:")
print("  python run.py")
print("\nTo build an executable:")
print("  python build.py")
print("\nFor more information, see README_APP.md")
print()
