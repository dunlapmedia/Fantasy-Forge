#!/usr/bin/env python3
"""Demo script showcasing Fantasy Forge features."""

from fantasy_forge.models.world import World, Race, MagicSystem, Location, TimelineEvent
from fantasy_forge.models.character import Character, CharacterRelationship
from fantasy_forge.models.manuscript import Manuscript, Chapter, Scene, Outline, PlotPoint
from fantasy_forge.services.storage_service import StorageService

print("=" * 70)
print("Fantasy Forge - Demo: Creating a Fantasy Story")
print("=" * 70)
print()

# Initialize storage
storage = StorageService("demo_data")
print("✓ Storage initialized in 'demo_data/' directory")
print()

# Create a fantasy world
print("Creating Fantasy World: 'The Shattered Realms'")
print("-" * 70)

world = World(
    name="The Shattered Realms",
    description="A world torn apart by the Cataclysm, where floating islands drift through an endless sky and ancient magic still lingers in the ruins."
)

# Add races
world.races.append(Race(
    name="Skyborn",
    description="Winged humanoids who live on the highest floating islands",
    traits=["flight", "keen_vision", "lightweight_build"],
    culture="Nomadic sky-dwelling society",
    lifespan="150-200 years",
    appearance="Pale skin with large feathered wings, silver or golden eyes"
))

world.races.append(Race(
    name="Deepforged",
    description="Stout beings who dwell in underground cities beneath the floating islands",
    traits=["strength", "resilience", "craftmanship"],
    culture="Traditional clan-based society of master craftsmen",
    lifespan="200-300 years",
    appearance="Dark metallic skin, glowing runes, stocky build"
))

print(f"  Added {len(world.races)} races")

# Add magic system
world.magic_systems.append(MagicSystem(
    name="Shard Magic",
    description="Magic drawn from crystallized remnants of the pre-Cataclysm world",
    rules=[
        "Requires physical contact with a Shard crystal",
        "Power depends on Shard size and purity",
        "Each Shard has an elemental affinity",
        "Overuse causes crystal corruption"
    ],
    limitations=[
        "Cannot create matter from nothing",
        "Corrupted Shards can possess users",
        "Magic fades in Shard-less zones"
    ],
    source="Ancient world energy trapped in crystals"
))

print(f"  Added {len(world.magic_systems)} magic system")

# Add locations
world.locations.append(Location(
    name="Aeris Haven",
    description="The largest sky city, suspended between three massive floating islands",
    geography="Interconnected platforms and bridges spanning multiple islands",
    climate="Cool, windy, frequent storms",
    population="~50,000 (mixed Skyborn and Deepforged)",
    notable_features=["The Great Library", "Shard Markets", "Wind Temples"]
))

world.locations.append(Location(
    name="The Underdepths",
    description="Vast network of caverns and forges beneath the floating islands",
    geography="Interconnected tunnel systems and underground lakes",
    climate="Warm, humid, illuminated by bioluminescent fungi",
    population="~100,000 (primarily Deepforged)",
    notable_features=["The Eternal Forge", "Crystal Mines", "Underground Sea"]
))

print(f"  Added {len(world.locations)} locations")

# Add timeline
world.timeline.append(TimelineEvent(
    title="The Cataclysm",
    description="The world shattered into floating islands when ancient magic went awry",
    date="Year 0 (1000 years ago)",
    category="historical"
))

world.timeline.append(TimelineEvent(
    title="First Contact",
    description="Skyborn and Deepforged first meet and establish trade",
    date="Year 200",
    category="historical"
))

world.timeline.append(TimelineEvent(
    title="Present Day",
    description="Tensions rise as Shard deposits become scarce",
    date="Year 1000",
    category="current"
))

print(f"  Added {len(world.timeline)} timeline events")

# Save world
storage.save_world(world)
print("✓ World saved successfully")
print()

# Create characters
print("Creating Characters")
print("-" * 70)

char1 = Character(
    name="Aria Windrider",
    description="A young Skyborn scout with dreams of exploring the world below",
    race="Skyborn",
    age="23",
    occupation="Sky Scout",
    appearance="Silver-white wings, azure eyes, slight build with wind-swept blonde hair",
    personality="Curious, brave, sometimes reckless, compassionate",
    backstory="Orphaned during a storm, raised by the Sky Guard. Always wondered about the islands below.",
    goals=["Discover what caused the Cataclysm", "Bridge the gap between Skyborn and Deepforged"],
    fears=["Losing her wings", "Failing those who depend on her"],
    skills=["Expert flyer", "Navigation", "Storm reading", "Shard sensing"],
    arc="From naive dreamer to bridge between two peoples"
)

char1.relationships.append(CharacterRelationship(
    character_name="Throk Ironheart",
    relationship_type="companion",
    description="Deepforged engineer she rescued, becomes her closest friend"
))

storage.save_character(char1)
print(f"  Created: {char1.name} ({char1.race})")

char2 = Character(
    name="Throk Ironheart",
    description="A Deepforged engineer searching for a legendary Shard to save his dying clan",
    race="Deepforged",
    age="87",
    occupation="Master Engineer",
    appearance="Dark bronze skin with glowing blue runes, muscular build, braided beard",
    personality="Stubborn, loyal, practical, witty in a dry way",
    backstory="Last of his clan's master engineers. His home forge is failing due to Shard shortage.",
    goals=["Find the Primal Shard to restore his clan's forge", "Honor his ancestors"],
    fears=["His clan's extinction", "Failing his people"],
    skills=["Master craftsman", "Shard engineering", "Ancient lore", "Combat"],
    arc="From isolationist to understanding the value of cooperation"
)

char2.relationships.append(CharacterRelationship(
    character_name="Aria Windrider",
    relationship_type="companion",
    description="Skyborn scout who saved his life, challenges his prejudices"
))

storage.save_character(char2)
print(f"  Created: {char2.name} ({char2.race})")
print("✓ Characters saved successfully")
print()

# Create manuscript
print("Creating Manuscript: 'The Shattered Sky'")
print("-" * 70)

manuscript = Manuscript(
    title="The Shattered Sky",
    author="Demo Author",
    synopsis="When a Skyborn scout and a Deepforged engineer discover a conspiracy threatening all of the Shattered Realms, they must overcome centuries of prejudice to prevent a second Cataclysm.",
    genre="Fantasy",
    target_word_count=90000
)

# Create outline
manuscript.outline = Outline(
    title="The Shattered Sky Outline",
    premise="Two unlikely allies must stop a power-hungry faction from weaponizing ancient Shards",
    themes=["Unity through diversity", "Consequences of power", "Hope in darkness"],
    notes="Focus on character growth and world exploration"
)

manuscript.outline.plot_points.append(PlotPoint(
    title="Aria witnesses mysterious Shard activity",
    description="Strange pulses emanate from the Underdepths",
    category="inciting_incident",
    chapter=1
))

manuscript.outline.plot_points.append(PlotPoint(
    title="Aria saves Throk from a Shard explosion",
    description="Forms unlikely friendship",
    category="rising_action",
    chapter=2
))

manuscript.outline.plot_points.append(PlotPoint(
    title="Discovery of the conspiracy",
    description="The Council is hoarding Shards and experimenting with forbidden magic",
    category="rising_action",
    chapter=5
))

manuscript.outline.character_arcs = {
    "Aria Windrider": "Naive dreamer -> Bridge between peoples",
    "Throk Ironheart": "Isolationist -> Cooperative leader"
}

print("  Created outline with plot structure")

# Create sample chapters
chapter1 = Chapter(
    number=1,
    title="Wings Against the Storm",
    synopsis="Aria patrols the storm barriers and discovers strange energy readings from below",
    status="draft"
)

scene1 = Scene(
    title="Storm Patrol",
    content="""The wind howled past Aria's wings as she soared through the storm barrier. Below, the endless void between the floating islands churned with violet lightning. It was her favorite patrol route—dangerous, beautiful, and wonderfully lonely.

She banked left, following the prescribed path, when something caught her attention. A pulse of green light, emanating from the Underdepths far below. Green meant Shard energy, but this was different. Stronger. Wrong.

Aria folded her wings and dove toward the light, her training forgotten in her curiosity. The wind screamed past her ears as she plummeted through the clouds. She had to know what it was.

That decision would change everything.""",
    pov_character="Aria Windrider",
    location="Sky Barrier above Aeris Haven"
)

chapter1.scenes.append(scene1)
chapter1.calculate_word_count()
manuscript.chapters.append(chapter1)
print(f"  Created Chapter 1: {chapter1.title} ({chapter1.word_count} words)")

chapter2 = Chapter(
    number=2,
    title="Fire and Stone",
    synopsis="Aria discovers Throk trapped in a collapsed mine, leading to an explosive first meeting",
    status="draft"
)

scene2 = Scene(
    title="The Rescue",
    content="""The green pulse led Aria to an old mine entrance, half-collapsed and smoking. Against every instinct, she landed and furled her wings tight against her back. Skyborn didn't go underground. It was wrong, unnatural.

"Hello?" she called into the darkness.

A groan answered her. Deep, pained, definitely Deepforged. She should leave, call the Guard, let them handle it. But the second pulse of energy knocked her off her feet, and she heard the mine begin to collapse.

She ran into the darkness.

What she found was a Deepforged engineer, pinned under rubble, surrounded by cracked Shards leaking dangerous energy. His eyes met hers—surprise, pain, suspicion.

"Let me help you," she said, reaching for him.

"You're Skyborn," he growled. "Your kind don't help mine."

"Well, I'm not very good at being Skyborn then," Aria replied, grabbing his arm.""",
    pov_character="Aria Windrider",
    location="Abandoned mine in the Underdepths"
)

chapter2.scenes.append(scene2)
chapter2.calculate_word_count()
manuscript.chapters.append(chapter2)
print(f"  Created Chapter 2: {chapter2.title} ({chapter2.word_count} words)")

manuscript.calculate_word_count()
storage.save_manuscript(manuscript)
print(f"✓ Manuscript saved successfully ({manuscript.word_count} words)")
print()

# Summary
print("=" * 70)
print("Demo Complete!")
print("=" * 70)
print()
print("Created:")
print(f"  • 1 World: {world.name}")
print(f"    - {len(world.races)} races")
print(f"    - {len(world.magic_systems)} magic system")
print(f"    - {len(world.locations)} locations")
print(f"    - {len(world.timeline)} timeline events")
print()
print(f"  • 2 Characters:")
print(f"    - {char1.name} ({char1.race})")
print(f"    - {char2.name} ({char2.race})")
print()
print(f"  • 1 Manuscript: {manuscript.title}")
print(f"    - {len(manuscript.chapters)} chapters")
print(f"    - {manuscript.word_count} words written")
print()
print("All data saved to 'demo_data/' directory")
print()
print("To view this data:")
print("  1. Run: python run.py")
print("  2. Navigate through the tabs to see the created content")
print("  3. Load saved items from the left panel of each tab")
print()
print("Happy writing! 🏰✨📖")
