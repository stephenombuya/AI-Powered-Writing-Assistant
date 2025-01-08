import spacy
import language_tool_python
from typing import List, Dict

class GrammarChecker:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.tool = language_tool_python.LanguageTool('en-US')
    
    def check_grammar(self, text: str) -> List[Dict]:
        """Check grammar and spelling in the text."""
        matches = self.tool.check(text)
        return [
            {
                'message': match.message,
                'replacements': match.replacements,
                'offset': match.offset,
                'length': match.errorLength,
                'category': match.category,
                'rule_id': match.ruleId
            }
            for match in matches
        ]
    
    def suggest_corrections(self, text: str) -> Dict:
        """Suggest corrections for the text."""
        doc = self.nlp(text)
        suggestions = []
        
        # Check sentence structure
        for sent in doc.sents:
            if len(sent) > 40:  # Long sentence
                suggestions.append({
                    'type': 'structure',
                    'text': sent.text,
                    'suggestion': 'Consider breaking this long sentence into smaller ones.'
                })
        
        return {
            'grammar_checks': self.check_grammar(text),
            'structure_suggestions': suggestions
        }
