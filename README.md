# AI-Powered Writing Assistant

An advanced writing assistant that helps users improve their writing through grammar checking, style analysis, and intelligent suggestions.

## Features

### Text Analysis
- Grammar and spelling check
- Sentence structure analysis
- Style and tone recommendations
- Readability scoring

### Content Enhancement
- Sentence rephrasing suggestions
- Vocabulary improvements
- Tone and sentiment analysis
- Writing style recommendations

### Document Management
- Export to Word (.docx) and PDF formats
- Document version history
- Progress tracking
- Cloud storage integration

## Technical Stack

- **Backend**: Python, Flask
- **NLP**: SpaCy, TextBlob
- **Grammar Checking**: language-tool-python
- **Document Processing**: python-docx, fpdf
- **Database**: SQLAlchemy with SQLite
- **Testing**: pytest

## Installation

1. Clone the repository:
```bash
git clone https://github.com/stephenombuya/AI-Powered-Writing-Assistant
cd writing-assistant
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download SpaCy model:
```bash
python -m spacy download en_core_web_sm
```

5. Initialize database:
```bash
flask db upgrade
```

## Usage

1. Start the server:
```bash
flask run
```

2. API Endpoints:

- Analyze text:
```bash
POST /analyze
{
    "text": "Your text here",
    "title": "Document Title"
}
```

- Export document:
```bash
POST /export/{document_id}
{
    "format": "docx" # or "pdf"
}
```

## Development

- Run tests:
```bash
pytest
```

- Format code:
```bash
black .
```

## Project Structure

```
writing-assistant/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── text_processor/
│   │   ├── __init__.py
│   │   ├── grammar_checker.py
│   │   ├── text_analyzer.py
│   │   └── document_exporter.py
│   └── utils.py
├── tests/
├── requirements.txt
└── README.md
```

## Analysis Features

### Grammar Checking
- Spelling errors
- Grammar mistakes
- Punctuation issues
- Style inconsistencies

### Text Analysis
- Sentiment analysis
- Tone detection
- Readability scoring
- Sentence complexity analysis

### Document Export
- Microsoft Word (.docx) format
- PDF format
- Formatted output
- Preservation of styling

## Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-feature`
3. Commit changes: `git commit -am 'Add new feature'`
4. Push to branch: `git push origin feature/new-feature`
5. Submit pull request

## License

This project is licensed under the GNU General Public License - see the `LICENSE` file for details.

## Future Improvements

- Add support for more languages
- Implement machine learning for better suggestions
- Add plagiarism detection
- Create browser extension
- Add real-time collaboration features
- Implement advanced text analytics
- Add support for more export formats
