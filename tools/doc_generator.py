from docx import Document
from docx.shared import Pt
import os

def create_admission_report(university, program, content, output_path):
    doc = Document()
    
    # Title
    title = doc.add_heading(f'Admissions Strategy: {university}', 0)
    doc.add_heading(f'Program: {program}', level=1)
    
    # Add the content
    # (Note: This is a simple version. For complex Markdown, you might want to split by '\n')
    p = doc.add_paragraph(content)
    
    # Save
    doc.save(output_path)
    return output_path