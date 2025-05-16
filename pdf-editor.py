from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from PyPDF2 import PdfReader, PdfWriter
from dotenv import load_dotenv
from io import BytesIO
import os

load_dotenv()
NAME = os.getenv("NAME")
SURNAME = os.getenv("SURNAME")
CODFISC = os.getenv("CODFISC")
DAY = os.getenv("DAY")
MONTH = os.getenv("MONTH")
YEAR = os.getenv("YEAR")
PLACE = os.getenv("PLACE")
PROV = os.getenv("PROV")


def crea_overlay_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    # Registra un font personalizzato (usa Arial se disponibile, altrimenti Helvetica)
    try:
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        c.setFont("Arial", 12)
    except:
        c.setFont("Helvetica", 12)

    # Scrive il contenuto nei punti desiderati
    c.drawString(185, 685, f"{SURNAME} {NAME}")
    c.drawString(185, 673, f"{CODFISC}")
    c.drawString(110, 597, f"{DAY}/{MONTH}/{YEAR}")
    c.drawString(240, 597, f"{PLACE}")
    c.drawString(380, 597, f"{PROV}")

    # Cambia colore e scrive un avviso
    #c.setFillColor(colors.red)
    #c.drawString(100, 690, "Attenzione: dati riservati")

    c.save()
    buffer.seek(0)
    return buffer

def scrivi_su_pdf_esistente(pdf_input, pdf_output):
    reader = PdfReader(pdf_input)
    writer = PdfWriter()

    overlay_pdf = PdfReader(crea_overlay_pdf())
    overlay_page = overlay_pdf.pages[0]

    for i, page in enumerate(reader.pages):
        # unisce l’overlay solo alla prima pagina (modificare se serve su tutte)
        nuova_pagina = page
        if i == 0:
            nuova_pagina.merge_page(overlay_page)
        writer.add_page(nuova_pagina)

    with open(pdf_output, "wb") as f:
        writer.write(f)
    print(f"PDF compilato salvato come: {pdf_output}")

# ESEMPIO DI USO
scrivi_su_pdf_esistente("1) PREASSUNTIVI AUTONOMI OCCASIONALI.pdf", "modulo_compilato.pdf")
