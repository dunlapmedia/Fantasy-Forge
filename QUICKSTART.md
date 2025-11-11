# Fantasy Forge - Quick Start Guide

Get started with Fantasy Forge in 5 minutes!

## Installation

```bash
# 1. Clone the repository
git clone https://github.com/dunlapmedia/Fantasy-Forge.git
cd Fantasy-Forge

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the application
python run.py
```

## First Steps

### Try the Demo

Run the demo to see example content:

```bash
python demo.py
```

This creates:
- A fantasy world with races, magic systems, and locations
- Two characters with detailed profiles
- A manuscript with 2 sample chapters

Then launch the app to explore the demo data:

```bash
python run.py
```

### Create Your Own Story

#### 1. Start the Application

```bash
python run.py
```

#### 2. Create a New World

1. Click the **"🌍 World Building"** tab
2. Click **"New World"**
3. Enter your world name (e.g., "My Fantasy Realm")
4. Add races, magic systems, and locations
5. Click **"Save World"**

#### 3. Create Characters

1. Click the **"👤 Characters"** tab
2. Click **"New Character"**
3. Fill in character details
4. Click **"Save Character"**

#### 4. Write Your Manuscript

1. Click the **"📝 Manuscript"** tab
2. Enter title, author, and synopsis
3. Click **"Add Chapter"**
4. Select the chapter and write your content
5. Click **"Update Chapter"**
6. Click **"Save Manuscript"**

## Using AI Features

Fantasy Forge integrates with Ollama for AI-powered features.

### Install Ollama

1. Download from [ollama.ai](https://ollama.ai)
2. Install and start Ollama
3. Pull a model: `ollama pull llama2`
4. Run Fantasy Forge

### AI Features Available

- **Writing Prompts**: Get inspiration (Manuscript tab)
- **Name Generators**: Generate character/location names
- **World Elements**: Generate races, magic systems, etc.
- **Text Analysis**: Dialogue and consistency checking (Tools tab)

Check **Help > Ollama Status** to verify connection.

## Key Features Overview

### 📝 Manuscript Tab
- Write chapters and scenes
- Track word count progress
- Get AI writing prompts
- Save/load manuscripts

### 🌍 World Building Tab
- Create fantasy worlds
- Add races with traits and cultures
- Design magic systems
- Map locations
- Generate elements with AI

### 👤 Characters Tab
- Build character profiles
- Define personality, backstory, appearance
- Track relationships
- Generate names with AI

### 🛠️ Tools Tab

**Text Analysis:**
- Word count and readability
- Repetition detection
- Passive voice detection

**AI Tools:**
- Dialogue analysis
- Consistency checking
- Writing suggestions

**Generators:**
- Names (characters, places)
- Magic items
- Quests
- Creatures

## Keyboard Shortcuts

- **Ctrl+N** - New Project
- **Ctrl+S** - Save
- **Ctrl+D** - Toggle Dark Mode
- **Ctrl+Q** - Quit

## Tips for Success

### Worldbuilding
- Start with broad concepts (races, magic)
- Add details gradually
- Use AI generators for inspiration
- Keep notes in the description fields

### Character Development
- Focus on personality and goals first
- Define clear character arcs
- Use relationships to add depth
- Save frequently

### Writing
- Set a target word count
- Break work into chapters
- Use writing prompts when stuck
- Analyze text regularly for improvement

### Organization
- Use consistent naming
- Save different versions with date stamps
- Back up your data/ directory
- Export important content regularly

## Troubleshooting

### "Ollama is not available"
- Install Ollama from ollama.ai
- Start Ollama: `ollama serve`
- Pull a model: `ollama pull llama2`

### "Failed to save"
- Check file permissions
- Ensure disk space available
- Try a different file name

### Application won't start
- Verify Python 3.10+ installed
- Install dependencies: `pip install -r requirements.txt`
- Check for error messages

## Building Executables

Create a standalone executable:

```bash
python build.py
```

The executable will be in the `dist/` directory.

### Platform-Specific Notes

**Windows:**
- Executable: `dist/Fantasy-Forge.exe`
- May need to allow through Windows Defender

**macOS:**
- Executable: `dist/Fantasy-Forge`
- May need to allow in Security & Privacy settings

**Linux:**
- Executable: `dist/Fantasy-Forge`
- May need to make executable: `chmod +x dist/Fantasy-Forge`

## Data Storage

All data is stored in JSON format in the `data/` directory:

```
data/
├── worlds/          # World building data
├── characters/      # Character profiles
└── manuscripts/     # Manuscript files
```

**Backup:** Simply copy the entire `data/` directory

**Export:** JSON files can be opened in any text editor

## Next Steps

- Read [README_APP.md](README_APP.md) for comprehensive documentation
- Explore all tabs and features
- Try the demo for inspiration
- Start your epic fantasy story!

## Support

- 📖 [Full Documentation](README_APP.md)
- 🐛 [Report Issues](https://github.com/dunlapmedia/Fantasy-Forge/issues)
- 💡 [Request Features](https://github.com/dunlapmedia/Fantasy-Forge/issues)

---

**Happy Writing! May your imagination soar and your worlds be boundless!** 🏰✨📖
