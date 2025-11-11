"""Ollama AI service integration."""

import requests
from typing import Optional, List, Dict
import json


class OllamaService:
    """Service for interacting with local Ollama instance."""

    def __init__(self, base_url: str = "http://localhost:11434"):
        """Initialize Ollama service.
        
        Args:
            base_url: Base URL for Ollama API
        """
        self.base_url = base_url
        self.model = "llama2"  # Default model

    def is_available(self) -> bool:
        """Check if Ollama is available."""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=2)
            return response.status_code == 200
        except:
            return False

    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> Optional[str]:
        """Generate text using Ollama.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system prompt
            
        Returns:
            Generated text or None if failed
        """
        try:
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            }
            
            if system_prompt:
                payload["system"] = system_prompt
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                return response.json().get("response", "")
            return None
        except Exception as e:
            print(f"Error generating text: {e}")
            return None

    def generate_writing_prompt(self, genre: str = "fantasy", theme: Optional[str] = None) -> str:
        """Generate a creative writing prompt.
        
        Args:
            genre: Genre for the prompt
            theme: Optional theme
            
        Returns:
            Generated prompt
        """
        system_prompt = "You are a creative writing assistant specializing in fantasy fiction."
        
        prompt = f"Generate a creative writing prompt for a {genre} story"
        if theme:
            prompt += f" with the theme of {theme}"
        prompt += ". Make it inspiring and specific."
        
        result = self.generate(prompt, system_prompt)
        return result if result else "A mysterious traveler arrives in a village with a secret that could change everything."

    def generate_character_name(self, race: str = "human", culture: str = "") -> str:
        """Generate a fantasy character name.
        
        Args:
            race: Character race
            culture: Cultural background
            
        Returns:
            Generated name
        """
        system_prompt = "You are a fantasy name generator. Provide only the name, nothing else."
        
        prompt = f"Generate a fantasy character name for a {race}"
        if culture:
            prompt += f" from {culture} culture"
        prompt += ". Provide only the name."
        
        result = self.generate(prompt, system_prompt)
        return result.strip() if result else "Unnamed"

    def generate_location_name(self, location_type: str = "city") -> str:
        """Generate a fantasy location name.
        
        Args:
            location_type: Type of location (city, forest, mountain, etc.)
            
        Returns:
            Generated name
        """
        system_prompt = "You are a fantasy location name generator. Provide only the name, nothing else."
        
        prompt = f"Generate a fantasy {location_type} name. Provide only the name."
        
        result = self.generate(prompt, system_prompt)
        return result.strip() if result else "Unnamed Location"

    def analyze_dialogue(self, dialogue: str, character_name: str, personality: str) -> str:
        """Analyze dialogue for character consistency.
        
        Args:
            dialogue: The dialogue text
            character_name: Character name
            personality: Character personality description
            
        Returns:
            Analysis feedback
        """
        system_prompt = "You are a writing editor specializing in character dialogue analysis."
        
        prompt = f"""Analyze this dialogue for the character {character_name} who has this personality: {personality}

Dialogue:
{dialogue}

Provide brief feedback on whether the dialogue matches the character's personality and suggestions for improvement."""
        
        result = self.generate(prompt, system_prompt)
        return result if result else "Unable to analyze dialogue at this time."

    def check_consistency(self, text: str, terms: List[str]) -> str:
        """Check text for consistency in terminology.
        
        Args:
            text: Text to check
            terms: List of terms to check for consistency
            
        Returns:
            Consistency analysis
        """
        system_prompt = "You are a writing editor checking for consistency."
        
        terms_str = ", ".join(terms)
        prompt = f"""Check this text for consistency in the use of these terms: {terms_str}

Text:
{text}

Report any inconsistencies or variations in how these terms are used."""
        
        result = self.generate(prompt, system_prompt)
        return result if result else "Unable to check consistency at this time."

    def generate_world_element(self, element_type: str, context: str = "") -> str:
        """Generate a fantasy world element.
        
        Args:
            element_type: Type of element (magic_system, race, culture, etc.)
            context: Additional context
            
        Returns:
            Generated element description
        """
        system_prompt = "You are a fantasy worldbuilding assistant."
        
        prompt = f"Generate a creative {element_type} for a fantasy world"
        if context:
            prompt += f". Context: {context}"
        prompt += ". Provide a name and brief description."
        
        result = self.generate(prompt, system_prompt)
        return result if result else f"A unique {element_type} waiting to be defined."
