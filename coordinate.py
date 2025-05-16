from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def crea_griglia_overlay(larghezza, altezza, step=20):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=(larghezza, altezza))
    c.setFont("Helvetica", 4)
    c.setStrokeColorRGB(0.7, 0.7, 0.7)  # grigio chiaro
    c.setFillColorRGB(0.4, 0.4, 0.4)    # testo più visibile

    for x in range(0, int(larghezza), step):
        c.drawString(x + 1, 2, str(x))
        c.line(x, 0, x, altezza)
    for y in range(0, int(altezza), step):
        c.drawString(2, y + 1, str(y))
        c.line(0, y, larghezza, y)

    c.save()
    buffer.seek(0)
    return buffer

def sovrapponi_griglia(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for pagina in reader.pages:
        larghezza = float(pagina.mediabox.width)
        altezza = float(pagina.mediabox.height)

        # crea griglia fitta
        overlay_buffer = crea_griglia_overlay(larghezza, altezza, step=20)
        overlay_reader = PdfReader(overlay_buffer)
        overlay_page = overlay_reader.pages[0]

        pagina.merge_page(overlay_page)
        writer.add_page(pagina)

    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"PDF con griglia precisa salvato come: {output_pdf}")

# ESEMPIO USO
sovrapponi_griglia("1) PREASSUNTIVI AUTONOMI OCCASIONALI.pdf", "modulo_griglia_fitta.pdf")
