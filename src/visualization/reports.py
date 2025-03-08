from fpdf import FPDF
import os

class PDFReport:
    def __init__(self, title):
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, title, ln=True, align='C')
        self.pdf.ln(10)

    def add_section(self, title, content):
        self.pdf.set_font("Arial", 'B', 12)
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, content)
        self.pdf.ln(5)

    def save(self, filename):
        self.pdf.output(filename)

def generate_report(data, filename):
    report = PDFReport("Market Research Report")
    
    for section_title, section_content in data.items():
        report.add_section(section_title, section_content)
    
    report.save(filename)

def create_report_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)