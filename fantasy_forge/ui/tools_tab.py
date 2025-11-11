"""Tools and utilities tab."""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTextEdit, QGroupBox, QMessageBox, QTabWidget
)
from PyQt6.QtCore import Qt

from fantasy_forge.services.ollama_service import OllamaService
from fantasy_forge.utils.text_analysis import TextAnalyzer


class ToolsTab(QWidget):
    """Tools and utilities tab."""

    def __init__(self, ollama_service: OllamaService):
        super().__init__()
        self.ollama_service = ollama_service
        self.text_analyzer = TextAnalyzer()
        self._setup_ui()

    def _setup_ui(self):
        """Setup UI components."""
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create tabs for different tool categories
        tabs = QTabWidget()
        layout.addWidget(tabs)

        # Text Analysis tab
        analysis_tab = self._create_analysis_tab()
        tabs.addTab(analysis_tab, "📊 Text Analysis")

        # AI Tools tab
        ai_tab = self._create_ai_tools_tab()
        tabs.addTab(ai_tab, "🤖 AI Tools")

        # Generators tab
        generator_tab = self._create_generator_tab()
        tabs.addTab(generator_tab, "✨ Generators")

    def _create_analysis_tab(self) -> QWidget:
        """Create text analysis tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Input area
        input_group = QGroupBox("Text to Analyze")
        input_layout = QVBoxLayout()
        input_group.setLayout(input_layout)

        self.analysis_input = QTextEdit()
        self.analysis_input.setPlaceholderText("Paste your text here for analysis...")
        input_layout.addWidget(self.analysis_input)

        layout.addWidget(input_group)

        # Analysis buttons
        btn_layout = QHBoxLayout()

        word_count_btn = QPushButton("Word Count")
        word_count_btn.clicked.connect(self._analyze_word_count)
        btn_layout.addWidget(word_count_btn)

        repetition_btn = QPushButton("Find Repetitions")
        repetition_btn.clicked.connect(self._find_repetitions)
        btn_layout.addWidget(repetition_btn)

        readability_btn = QPushButton("Readability")
        readability_btn.clicked.connect(self._analyze_readability)
        btn_layout.addWidget(readability_btn)

        passive_btn = QPushButton("Detect Passive Voice")
        passive_btn.clicked.connect(self._detect_passive_voice)
        btn_layout.addWidget(passive_btn)

        layout.addLayout(btn_layout)

        # Results area
        results_group = QGroupBox("Analysis Results")
        results_layout = QVBoxLayout()
        results_group.setLayout(results_layout)

        self.analysis_results = QTextEdit()
        self.analysis_results.setReadOnly(True)
        results_layout.addWidget(self.analysis_results)

        layout.addWidget(results_group)

        return widget

    def _create_ai_tools_tab(self) -> QWidget:
        """Create AI tools tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Input area
        input_group = QGroupBox("Input")
        input_layout = QVBoxLayout()
        input_group.setLayout(input_layout)

        self.ai_input = QTextEdit()
        self.ai_input.setPlaceholderText("Enter text for AI analysis...")
        input_layout.addWidget(self.ai_input)

        layout.addWidget(input_group)

        # AI tool buttons
        btn_layout = QHBoxLayout()

        dialogue_btn = QPushButton("Analyze Dialogue")
        dialogue_btn.clicked.connect(self._analyze_dialogue_ai)
        btn_layout.addWidget(dialogue_btn)

        consistency_btn = QPushButton("Check Consistency")
        consistency_btn.clicked.connect(self._check_consistency_ai)
        btn_layout.addWidget(consistency_btn)

        improve_btn = QPushButton("Suggest Improvements")
        improve_btn.clicked.connect(self._suggest_improvements)
        btn_layout.addWidget(improve_btn)

        layout.addLayout(btn_layout)

        # Results area
        results_group = QGroupBox("AI Analysis Results")
        results_layout = QVBoxLayout()
        results_group.setLayout(results_layout)

        self.ai_results = QTextEdit()
        self.ai_results.setReadOnly(True)
        results_layout.addWidget(self.ai_results)

        layout.addWidget(results_group)

        return widget

    def _create_generator_tab(self) -> QWidget:
        """Create generators tab."""
        widget = QWidget()
        layout = QVBoxLayout()
        widget.setLayout(layout)

        layout.addWidget(QLabel("<h3>Fantasy Element Generators</h3>"))
        layout.addWidget(QLabel("Generate random fantasy elements using AI"))

        # Generator buttons
        btn_group = QGroupBox("Generators")
        btn_layout = QVBoxLayout()
        btn_group.setLayout(btn_layout)

        generators = [
            ("Generate Character Name", self._generate_name),
            ("Generate Place Name", self._generate_place),
            ("Generate Magic Item", self._generate_magic_item),
            ("Generate Quest Hook", self._generate_quest),
            ("Generate Creature", self._generate_creature),
        ]

        for label, handler in generators:
            btn = QPushButton(label)
            btn.clicked.connect(handler)
            btn_layout.addWidget(btn)

        layout.addWidget(btn_group)

        # Results area
        results_group = QGroupBox("Generated Content")
        results_layout = QVBoxLayout()
        results_group.setLayout(results_layout)

        self.generator_results = QTextEdit()
        self.generator_results.setReadOnly(True)
        results_layout.addWidget(self.generator_results)

        layout.addWidget(results_group)

        layout.addStretch()

        return widget

    # Text Analysis Methods
    def _analyze_word_count(self):
        """Analyze word count and basic metrics."""
        text = self.analysis_input.toPlainText()
        if not text:
            self.analysis_results.setText("Please enter text to analyze.")
            return

        metrics = self.text_analyzer.calculate_readability_score(text)
        
        result = f"""Word Count Analysis:
        
Total Words: {metrics['total_words']}
Total Sentences: {metrics['total_sentences']}
Average Sentence Length: {metrics['avg_sentence_length']} words
Average Word Length: {metrics['avg_word_length']} characters
"""
        self.analysis_results.setText(result)

    def _find_repetitions(self):
        """Find repeated words and phrases."""
        text = self.analysis_input.toPlainText()
        if not text:
            self.analysis_results.setText("Please enter text to analyze.")
            return

        repeated_words = self.text_analyzer.find_repeated_words(text)
        repeated_phrases = self.text_analyzer.find_repeated_phrases(text)

        result = "Repetition Analysis:\n\n"
        
        result += "Most Repeated Words:\n"
        for word, count in repeated_words[:10]:
            result += f"  • {word}: {count} times\n"
        
        result += "\nMost Repeated Phrases:\n"
        for phrase, count in repeated_phrases[:10]:
            result += f"  • \"{phrase}\": {count} times\n"

        self.analysis_results.setText(result)

    def _analyze_readability(self):
        """Analyze readability."""
        text = self.analysis_input.toPlainText()
        if not text:
            self.analysis_results.setText("Please enter text to analyze.")
            return

        metrics = self.text_analyzer.calculate_readability_score(text)
        
        result = f"""Readability Analysis:

Average Sentence Length: {metrics['avg_sentence_length']} words
  • Ideal: 15-20 words per sentence
  • Your text: {"Good" if 10 <= metrics['avg_sentence_length'] <= 25 else "Could be improved"}

Average Word Length: {metrics['avg_word_length']} characters
  • Your text uses {"simple" if metrics['avg_word_length'] < 5 else "moderate" if metrics['avg_word_length'] < 6 else "complex"} vocabulary

Total Sentences: {metrics['total_sentences']}
Total Words: {metrics['total_words']}
"""
        self.analysis_results.setText(result)

    def _detect_passive_voice(self):
        """Detect passive voice in text."""
        text = self.analysis_input.toPlainText()
        if not text:
            self.analysis_results.setText("Please enter text to analyze.")
            return

        passive_sentences = self.text_analyzer.detect_passive_voice(text)

        result = "Passive Voice Detection:\n\n"
        
        if passive_sentences:
            result += f"Found {len(passive_sentences)} potential passive voice constructions:\n\n"
            for i, sentence in enumerate(passive_sentences, 1):
                result += f"{i}. {sentence}\n\n"
            result += "\nConsider revising these sentences to use active voice for stronger writing."
        else:
            result += "No obvious passive voice constructions detected. Good job!"

        self.analysis_results.setText(result)

    # AI Tools Methods
    def _analyze_dialogue_ai(self):
        """Analyze dialogue using AI."""
        if not self.ollama_service.is_available():
            self.ai_results.setText("Ollama is not available. Please start Ollama to use AI features.")
            return

        text = self.ai_input.toPlainText()
        if not text:
            self.ai_results.setText("Please enter dialogue to analyze.")
            return

        self.ai_results.setText("Analyzing dialogue with AI...")
        result = self.ollama_service.analyze_dialogue(text, "Character", "brave and witty")
        self.ai_results.setText(result)

    def _check_consistency_ai(self):
        """Check consistency using AI."""
        if not self.ollama_service.is_available():
            self.ai_results.setText("Ollama is not available. Please start Ollama to use AI features.")
            return

        text = self.ai_input.toPlainText()
        if not text:
            self.ai_results.setText("Please enter text to check.")
            return

        # Extract potential character names
        names = self.text_analyzer.extract_character_names(text)
        
        self.ai_results.setText("Checking consistency with AI...")
        result = self.ollama_service.check_consistency(text, names[:5])
        self.ai_results.setText(result)

    def _suggest_improvements(self):
        """Suggest improvements using AI."""
        if not self.ollama_service.is_available():
            self.ai_results.setText("Ollama is not available. Please start Ollama to use AI features.")
            return

        text = self.ai_input.toPlainText()
        if not text:
            self.ai_results.setText("Please enter text for improvement suggestions.")
            return

        prompt = f"""As a writing editor, provide brief suggestions to improve this fantasy fiction text:

{text}

Focus on: clarity, pacing, description, and engagement."""

        self.ai_results.setText("Generating suggestions with AI...")
        result = self.ollama_service.generate(prompt, "You are a helpful writing editor.")
        self.ai_results.setText(result if result else "Unable to generate suggestions.")

    # Generator Methods
    def _generate_name(self):
        """Generate character name."""
        if not self.ollama_service.is_available():
            self.generator_results.setText("Ollama is not available.")
            return

        name = self.ollama_service.generate_character_name()
        self.generator_results.setText(f"Character Name: {name}")

    def _generate_place(self):
        """Generate place name."""
        if not self.ollama_service.is_available():
            self.generator_results.setText("Ollama is not available.")
            return

        name = self.ollama_service.generate_location_name()
        self.generator_results.setText(f"Place Name: {name}")

    def _generate_magic_item(self):
        """Generate magic item."""
        if not self.ollama_service.is_available():
            self.generator_results.setText("Ollama is not available.")
            return

        result = self.ollama_service.generate_world_element("magic item")
        self.generator_results.setText(result)

    def _generate_quest(self):
        """Generate quest hook."""
        if not self.ollama_service.is_available():
            self.generator_results.setText("Ollama is not available.")
            return

        result = self.ollama_service.generate_world_element("quest hook")
        self.generator_results.setText(result)

    def _generate_creature(self):
        """Generate fantasy creature."""
        if not self.ollama_service.is_available():
            self.generator_results.setText("Ollama is not available.")
            return

        result = self.ollama_service.generate_world_element("fantasy creature")
        self.generator_results.setText(result)
