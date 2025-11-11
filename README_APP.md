# Fantasy Forge

A multifeatured, executable application for fantasy fiction writers with comprehensive worldbuilding and manuscript writing tools.

## Features

### 🌍 Worldbuilding Tools
- **Fantasy World Constructor**: Create and manage detailed fantasy worlds
  - Define races with cultures, traits, and characteristics
  - Design magic systems with rules and limitations
  - Map locations with geography, climate, and notable features
  - Build timelines of events
  
- **Interactive Map Editor**: Basic canvas for creating world maps (extensible)

- **Timeline Builder**: Chronological event organization for your story world

### 📝 Drafting Assistance
- **Smart Outlining**: Structure your story with plot points and character arcs
- **Chapter Tracking**: Organize and track progress across chapters
- **AI-Powered Writing Prompts**: Get creative inspiration using Ollama
- **Word Count Tracking**: Monitor progress toward your writing goals

### ✍️ Editing Features
- **Grammar and Style Checker**: Basic text analysis tools
- **Repetition Detection**: Find overused words and phrases
- **Consistency Checker**: Ensure consistent use of names and terms
- **Readability Analysis**: Evaluate sentence length and complexity
- **Passive Voice Detection**: Identify passive constructions

### 👤 Character Development
- **Character Profile Builder**: Create detailed character profiles
  - Backstory, personality, and appearance
  - Goals, fears, and skills
  - Relationships and character arcs
- **Dialogue Analysis**: AI-powered feedback on character dialogue

### 🔧 Research and Reference Tools
- **Text Analysis**: Word counts, readability metrics, repetition detection
- **AI Generators**: Generate names, locations, items, quests, and creatures
- **Bookmarks and Annotations**: Track important sections (via notes)

### 🤖 AI Integration
- **Local Ollama Integration**: Uses your local Ollama instance
- **Creative Generators**: Names, locations, magic items, creatures
- **Writing Assistance**: Prompts, dialogue analysis, consistency checking
- **Worldbuilding Support**: Generate fantasy elements on demand

### 💾 Data Management
- **JSON-based Storage**: Simple, readable data format
- **Auto-save Support**: Save your work frequently
- **Cross-platform Compatible**: Works on Windows, macOS, and Linux

### 🎨 User Interface
- **Dark/Light Mode**: Toggle theme for comfortable writing sessions
- **Tabbed Interface**: Easy navigation between features
- **Intuitive Design**: Clean, focused writing environment

## Installation

### Prerequisites
- Python 3.10 or higher
- Ollama (optional, for AI features) - [Install Ollama](https://ollama.ai)

### Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dunlapmedia/Fantasy-Forge.git
   cd Fantasy-Forge
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python run.py
   ```

### Using a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

## Using Ollama for AI Features

Fantasy Forge integrates with Ollama for AI-powered features. To use these features:

1. **Install Ollama** from [ollama.ai](https://ollama.ai)

2. **Start Ollama** and pull a model:
   ```bash
   ollama pull llama2
   ```

3. **Run Fantasy Forge** - it will automatically detect the running Ollama instance

AI features will gracefully degrade if Ollama is not available.

## Usage Guide

### Creating a New Project

1. Launch Fantasy Forge
2. Use **File > New Project** to start fresh
3. Start with any tab:
   - **Manuscript**: Begin writing your story
   - **World Building**: Create your fantasy world
   - **Characters**: Develop your cast
   - **Tools**: Use analysis and generators

### World Building

1. Go to the **World Building** tab
2. Click "New World" and name your world
3. Add races, magic systems, and locations
4. Use "Generate (AI)" buttons for inspiration
5. Click "Save World" to persist your work

### Character Development

1. Go to the **Characters** tab
2. Click "New Character" and enter a name
3. Fill in character details (appearance, personality, backstory)
4. Use "Generate Name (AI)" for character names
5. Click "Save Character" to persist

### Writing Your Manuscript

1. Go to the **Manuscript** tab
2. Enter manuscript details (title, author, synopsis)
3. Click "Add Chapter" to create chapters
4. Select a chapter to edit its content
5. Click "Update Chapter" after making changes
6. Use "Get Writing Prompt (AI)" for inspiration
7. Click "Save Manuscript" to persist your work

### Using Analysis Tools

1. Go to the **Tools** tab
2. Select the **Text Analysis** sub-tab
3. Paste text to analyze
4. Click analysis buttons (Word Count, Repetitions, etc.)
5. Review results and improve your writing

### Using AI Tools

1. Ensure Ollama is running
2. Go to **Tools > AI Tools** tab
3. Enter text for AI analysis
4. Use analysis features or generators
5. Apply suggestions to your writing

## Building Executables

To create standalone executables for distribution:

### Using PyInstaller

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable (Windows)
pyinstaller --name="Fantasy-Forge" --windowed --icon=icon.ico run.py

# Build executable (macOS)
pyinstaller --name="Fantasy-Forge" --windowed --icon=icon.icns run.py

# Build executable (Linux)
pyinstaller --name="Fantasy-Forge" --windowed run.py
```

The executable will be in the `dist/` directory.

## Data Storage

Fantasy Forge stores data in the `data/` directory:
- `data/worlds/` - World building data
- `data/characters/` - Character profiles
- `data/manuscripts/` - Manuscript files

All data is saved in JSON format for easy backup and portability.

## Keyboard Shortcuts

- **Ctrl+N** - New Project
- **Ctrl+O** - Open Project
- **Ctrl+S** - Save
- **Ctrl+D** - Toggle Dark Mode
- **Ctrl+Q** - Quit

## Troubleshooting

### Ollama Connection Issues
- Ensure Ollama is running: `ollama serve`
- Check Ollama is accessible at `http://localhost:11434`
- View status via **Help > Ollama Status**

### Missing Dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Display Issues
- Try toggling dark/light mode (Ctrl+D)
- Check PyQt6 is properly installed

## Future Enhancements

Potential features for future versions:
- Enhanced map editor with drawing tools
- Collaboration features (multi-user support)
- Cloud synchronization
- Export to various formats (PDF, EPUB, etc.)
- Advanced grammar checking
- Version control for manuscripts
- Character relationship graphs
- Plot structure visualization

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source. See LICENSE file for details.

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check the documentation
- Review the help menu in the application

## Credits

Developed using:
- Python 3.10+
- PyQt6 for the GUI
- Ollama for AI features
- NLTK for text analysis

---

**Happy Writing! May your stories be epic and your worlds be boundless!** 🏰✨📖
