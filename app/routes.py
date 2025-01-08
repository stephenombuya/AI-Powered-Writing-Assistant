from flask import Blueprint, request, jsonify
from .models import db, Document
from .text_processor.grammar_checker import GrammarChecker
from .text_processor.text_analyzer import TextAnalyzer
from .text_processor.document_exporter import DocumentExporter

bp = Blueprint('main', __name__)
grammar_checker = GrammarChecker()
text_analyzer = TextAnalyzer()
document_exporter = DocumentExporter()

@bp.route('/analyze', methods=['POST'])
def analyze_text():
    data = request.get_json()
    text = data.get('text')
    title = data.get('title', 'Untitled Document')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Perform analysis
    grammar_results = grammar_checker.suggest_corrections(text)
    analysis_results = text_analyzer.analyze_tone(text)
    
    # Save to database
    doc = Document(
        title=title,
        content=text,
        analysis_results={
            'grammar': grammar_results,
            'analysis': analysis_results
        }
    )
    db.session.add(doc)
    db.session.commit()
    
    return jsonify({
        'id': doc.id,
        'grammar_check': grammar_results,
        'analysis': analysis_results
    })

@bp.route('/export/<int:doc_id>', methods=['POST'])
def export_document(doc_id):
    data = request.get_json()
    format_type = data.get('format', 'docx')
    
    doc = Document.query.get_or_404(doc_id)
    
    if format_type == 'docx':
        filename = document_exporter.export_to_word(doc.content, doc.title)
    elif format_type == 'pdf':
        filename = document_exporter.export_to_pdf(doc.content, doc.title)
    else:
        return jsonify({'error': 'Unsupported format'}), 400
    
    return jsonify({
        'message': 'Document exported successfully',
        'filename': filename
    })
