"""Text analysis utilities."""

import re
from collections import Counter
from typing import List, Dict, Tuple


class TextAnalyzer:
    """Utility class for analyzing text."""

    @staticmethod
    def count_words(text: str) -> int:
        """Count words in text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Word count
        """
        return len(text.split())

    @staticmethod
    def find_repeated_words(text: str, min_length: int = 4, min_count: int = 3) -> List[Tuple[str, int]]:
        """Find repeated words in text.
        
        Args:
            text: Text to analyze
            min_length: Minimum word length to consider
            min_count: Minimum repetition count
            
        Returns:
            List of (word, count) tuples
        """
        words = re.findall(r'\b\w+\b', text.lower())
        words = [w for w in words if len(w) >= min_length]
        
        counter = Counter(words)
        repeated = [(word, count) for word, count in counter.items() if count >= min_count]
        repeated.sort(key=lambda x: x[1], reverse=True)
        
        return repeated

    @staticmethod
    def find_repeated_phrases(text: str, phrase_length: int = 2, min_count: int = 2) -> List[Tuple[str, int]]:
        """Find repeated phrases in text.
        
        Args:
            text: Text to analyze
            phrase_length: Number of words in phrase
            min_count: Minimum repetition count
            
        Returns:
            List of (phrase, count) tuples
        """
        words = re.findall(r'\b\w+\b', text.lower())
        
        phrases = []
        for i in range(len(words) - phrase_length + 1):
            phrase = ' '.join(words[i:i + phrase_length])
            phrases.append(phrase)
        
        counter = Counter(phrases)
        repeated = [(phrase, count) for phrase, count in counter.items() if count >= min_count]
        repeated.sort(key=lambda x: x[1], reverse=True)
        
        return repeated

    @staticmethod
    def check_term_consistency(text: str, terms: List[str]) -> Dict[str, List[str]]:
        """Check for inconsistent use of terms.
        
        Args:
            text: Text to analyze
            terms: List of terms to check
            
        Returns:
            Dictionary of term variations found
        """
        results = {}
        
        for term in terms:
            # Find all variations (case differences, with/without hyphen, etc.)
            pattern = re.compile(r'\b' + re.escape(term) + r'\b', re.IGNORECASE)
            matches = pattern.findall(text)
            
            unique_matches = list(set(matches))
            if len(unique_matches) > 1:
                results[term] = unique_matches
        
        return results

    @staticmethod
    def extract_character_names(text: str) -> List[str]:
        """Extract potential character names from text.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of potential character names
        """
        # Simple heuristic: capitalized words that aren't at sentence start
        sentences = text.split('.')
        names = []
        
        for sentence in sentences:
            words = sentence.split()
            for i, word in enumerate(words):
                if i > 0 and word[0].isupper() and len(word) > 2:
                    # Check if it's likely a name (not common words)
                    common_words = {'The', 'And', 'But', 'Or', 'So', 'Yet', 'For', 'Nor', 'At', 'By', 'From', 'In', 'Into', 'Of', 'On', 'To', 'With'}
                    if word not in common_words:
                        names.append(word)
        
        # Return unique names sorted by frequency
        counter = Counter(names)
        return [name for name, count in counter.most_common(20)]

    @staticmethod
    def calculate_readability_score(text: str) -> Dict[str, float]:
        """Calculate basic readability metrics.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary of readability metrics
        """
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        words = re.findall(r'\b\w+\b', text)
        
        if not sentences or not words:
            return {"avg_sentence_length": 0, "avg_word_length": 0}
        
        avg_sentence_length = len(words) / len(sentences)
        avg_word_length = sum(len(word) for word in words) / len(words)
        
        return {
            "avg_sentence_length": round(avg_sentence_length, 2),
            "avg_word_length": round(avg_word_length, 2),
            "total_sentences": len(sentences),
            "total_words": len(words),
        }

    @staticmethod
    def detect_passive_voice(text: str) -> List[str]:
        """Detect potential passive voice constructions.
        
        Args:
            text: Text to analyze
            
        Returns:
            List of sentences with potential passive voice
        """
        # Simple detection: "was/were/been" + past participle pattern
        passive_patterns = [
            r'\b(was|were|been)\s+\w+(ed|en|own|un)\b',
            r'\b(is|are|am|be)\s+being\s+\w+ed\b',
        ]
        
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
        passive_sentences = []
        
        for sentence in sentences:
            for pattern in passive_patterns:
                if re.search(pattern, sentence, re.IGNORECASE):
                    passive_sentences.append(sentence)
                    break
        
        return passive_sentences[:10]  # Limit to first 10 examples
