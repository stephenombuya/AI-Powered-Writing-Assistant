from textblob import TextBlob
import spacy
from typing import Dict

class TextAnalyzer:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    
    def analyze_tone(self, text: str) -> Dict:
        """Analyze the tone and sentiment of the text."""
        blob = TextBlob(text)
        doc = self.nlp(text)
        
        # Calculate sentiment polarity and subjectivity
        sentiment = blob.sentiment
        
        # Analyze readability
        sentences = list(doc.sents)
        words = len(text.split())
        avg_sentence_length = words / len(sentences) if sentences else 0
        
        return {
            'sentiment': {
                'polarity': sentiment.polarity,
                'subjectivity': sentiment.subjectivity
            },
            'readability': {
                'avg_sentence_length': avg_sentence_length,
                'flesch_reading_ease': self.calculate_flesch_reading_ease(text)
            },
            'tone_suggestions': self.generate_tone_suggestions(sentiment.polarity)
        }
    
    def calculate_flesch_reading_ease(self, text: str) -> float:
        """Calculate Flesch Reading Ease score."""
        blob = TextBlob(text)
        words = len(blob.words)
        sentences = len(blob.sentences)
        syllables = sum(self.count_syllables(word) for word in blob.words)
        
        if words == 0 or sentences == 0:
            return 0
            
        return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    
    def count_syllables(self, word: str) -> int:
        """Count syllables in a word."""
        count = 0
        vowels = 'aeiouy'
        word = word.lower()
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith('e'):
            count -= 1
        if count == 0:
            count += 1
        return count
    
    def generate_tone_suggestions(self, polarity: float) -> List[str]:
        """Generate tone-based suggestions."""
        suggestions = []
        if polarity < -0.5:
            suggestions.append("The tone is very negative. Consider using more positive language.")
        elif polarity < 0:
            suggestions.append("The tone is slightly negative. Consider balancing with some positive elements.")
        elif polarity > 0.5:
            suggestions.append("The tone is very positive. Ensure it matches your intended message.")
        return suggestions

