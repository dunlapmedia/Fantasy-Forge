# Fantasy Forge

A multifeatured, executable application for fantasy fiction writers with comprehensive worldbuilding and manuscript writing tools.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![PyQt6](https://img.shields.io/badge/PyQt6-6.6+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

Fantasy Forge is a desktop application designed specifically for fantasy fiction writers who need powerful tools for:
- **Worldbuilding** (races, magic systems, locations, timelines)
- **Character Development** (detailed profiles, relationships, arcs)
- **Manuscript Writing** (chapters, scenes, progress tracking)
- **AI-Powered Assistance** (via local Ollama integration)
- **Text Analysis** (repetition detection, readability, consistency)

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

For detailed installation and usage instructions, see [README_APP.md](README_APP.md).

## Features

### ✨ Worldbuilding Tools
- Create and manage fantasy worlds with races, magic systems, and locations
- Build timelines of events
- AI-powered world element generation

### 📝 Manuscript Tools
- Chapter and scene organization
- Word count tracking with progress bars
- Writing prompts from AI

### 👤 Character Development
- Detailed character profiles
- Backstory, personality, and appearance tracking
- Character relationship management

### 🔧 Analysis & Editing
- Word repetition detection
- Readability analysis
- Passive voice detection
- Consistency checking

### 🤖 AI Integration
- Uses local Ollama instance
- Generate names, locations, creatures, items, and quests
- Dialogue analysis and improvement suggestions

### 🎨 User Experience
- Dark/Light mode toggle
- Cross-platform (Windows, macOS, Linux)
- Intuitive tabbed interface
- JSON-based data storage

## Documentation

See [README_APP.md](README_APP.md) for comprehensive documentation including:
- Installation guide
- Feature walkthrough
- Ollama setup
- Building executables
- Troubleshooting

## Building Executables

```bash
python build.py
```

This creates a standalone executable in the `dist/` directory.

## Technology Stack

- **Python 3.10+**
- **PyQt6** - Cross-platform GUI framework
- **Ollama** - Local AI integration
- **NLTK** - Natural language processing
- **JSON** - Data persistence

## Project Structure

```
Fantasy-Forge/
├── fantasy_forge/           # Main application package
│   ├── models/             # Data models (World, Character, Manuscript)
│   ├── services/           # Services (Storage, Ollama)
│   ├── ui/                 # UI components (tabs, windows)
│   ├── utils/              # Utilities (text analysis)
│   └── main.py             # Application entry point
├── data/                   # Data storage (created at runtime)
├── requirements.txt        # Python dependencies
├── setup.py               # Package configuration
├── run.py                 # Convenience runner
├── build.py               # Executable build script
└── README_APP.md          # Comprehensive documentation

```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## License

Open source - see LICENSE for details.

## Support

- 📖 Read the [full documentation](README_APP.md)
- 🐛 Report issues on GitHub
- 💡 Suggest features via GitHub issues

---

**Start crafting your epic fantasy stories today!** 🏰✨📖