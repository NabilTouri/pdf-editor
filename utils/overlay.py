from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.utils import ImageReader

from io import BytesIO
from datetime import datetime
#base dir è sbagliato, perchè non è la cartella principale del progetto, è la cartella sopra
#quindi dobbiamo tornare indietro di un livello
BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = BASE_DIR / "input"
OUTPUT_DIR = BASE_DIR / "output"
IMAGE_DIR = BASE_DIR / "images"
SIGNATURE_PATH = IMAGE_DIR / "signature.png"

def first_overlay_pdf(data, index):
    anagrafica = data.Anagrafica()
    residenza = data.Residenza()
    professione = data.Professione()
    famiglia = data.Famiglia()
    banca = data.Banca()

    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    signature = ImageReader(str(SIGNATURE_PATH))
    orig_width, orig_height = signature.getSize()

    try:
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        c.setFont("Arial", 10)
    except:
        c.setFont("Helvetica", 10)
    
    if index == 0:
        # Scrive il contenuto nei punti desiderati
        c.drawString(185, 685, f"{anagrafica.cognome} {anagrafica.nome}")
        c.drawString(185, 673, f"{anagrafica.codfisc}")

        c.drawString(110, 598, f"{anagrafica.giorno}/{anagrafica.mese}/{anagrafica.anno}")
        c.drawString(240, 598, f"{anagrafica.luogo}")
        c.drawString(380, 598, f"{anagrafica.prov}")

        c.drawString(130, 585, f"{anagrafica.stato}")
        c.drawString(360, 585, f"{anagrafica.cittadinanza}")

        c.drawString(150, 530, f"{residenza.citta}")
        c.drawString(400, 530, f"{residenza.prov}")
        c.drawString(150, 517, f"{residenza.via} {residenza.num_civ}")
        c.drawString(400, 517, f"{residenza.cap}")
        c.drawString(150, 504, f"{residenza.stato}")

        c.drawString(150, 460, f"{residenza.citta}")
        c.drawString(400, 460, f"{residenza.prov}")
        c.drawString(150, 448, f"{residenza.via} {residenza.num_civ}")
        c.drawString(400, 448, f"{residenza.cap}")
        c.drawString(150, 435, f"{residenza.stato}")
        c.drawString(150, 420, f"{residenza.telefono}")
        c.drawString(150, 407, f"{residenza.email}")

        if anagrafica.cittadinanza.lower() == "italiana":
            c.drawString(98, 366, "X")
        else:
            c.drawString(293, 366, "X")
        c.drawString(98, 325, "X")
    elif index == 1:
        if professione.lavoro == "True":
            c.drawString(80, 730, "X")
        
        c.drawString(80, 627, "X")
        c.drawString(150,627, professione.tipo_scuola_attuale)
        c.drawString(350, 627, professione.nome_scuola_attuale)

        c.drawString(80, 570, "X")
        c.drawString(180, 570, professione.tipo_scuola_titolo)
        c.drawString(180, 543, professione.nome_scuola_titolo)
        c.drawString(390, 543, professione.data_titolo)

        y_start = 448
        y_step = 15
        for membro in famiglia.membri:
            c.drawString(80, y_start, membro['nome'])
            c.drawString(200, y_start, membro['data_nascita'])
            c.drawString(325, y_start, membro['luogo_nascita'])
            c.drawString(425, y_start, membro['parentela'])
            y_start -= y_step
        
        c.drawString(80, 315, "X")
        c.drawString(80, 300, "X")
        c.drawString(80, 285, "X")
        c.drawString(80, 240, "X")

        c.drawString(140, 183, datetime.now().strftime("%d/%m/%Y"))
        target_width = 90
        target_height = (target_width / orig_width) * orig_height
        c.drawImage(signature, 380, 183, width=target_width, height=target_height, mask='auto')
    elif index == 2:
        c.drawString(100, 704, "Brescia")
        #stampa solo il giorno di oggi
        c.drawString(210, 704, datetime.now().strftime("%d"))
        c.drawString(235, 704, datetime.now().strftime("%m"))
        c.drawString(270, 704, datetime.now().strftime("%Y"))

        c.drawString(170, 610, anagrafica.cognome)
        c.drawString(400, 610, anagrafica.nome)
        c.drawString(200, 583, f'{residenza.via} {residenza.num_civ}')
        c.drawString(170, 554, residenza.citta)
        c.drawString(370, 554, residenza.prov)
        c.drawString(460, 554, residenza.cap)

        c.setFontSize(12)
        x_start = 85
        x_step = 27
        for char in anagrafica.codfisc:
            c.drawString(x_start, 504, char)
            x_start += x_step
        c.setFontSize(10)

        c.drawString(170, 410, banca.nome)

        c.setFontSize(12)
        x_start = 82
        x_step = 16.2
        for char in banca.iban:
            c.drawString(x_start, 347, char)
            x_start += x_step
        c.setFontSize(10)
        
        target_width = 90
        target_height = (target_width / orig_width) * orig_height
        c.drawImage(signature, 360, 70, width=target_width, height=target_height, mask='auto')
    elif index == 3:
        c.drawString(100, 730, "Brescia")
        #stampa solo il giorno di oggi
        c.drawString(60, 704, datetime.now().strftime("%d"))
        c.drawString(85, 704, datetime.now().strftime("%m"))
        c.drawString(110, 704, datetime.now().strftime("%Y"))

        c.drawString(170, 447, f"{anagrafica.cognome} {anagrafica.nome}")
        c.drawString(440, 447, anagrafica.luogo)

        c.drawString(78, 431, anagrafica.giorno)
        c.drawString(120, 431, anagrafica.mese)
        c.drawString(160, 431, anagrafica.anno)

        c.drawString(67, 200, datetime.now().strftime("%d/%m/%Y"))
        target_width = 90
        target_height = (target_width / orig_width) * orig_height
        c.drawImage(signature, 420, 200, width=target_width, height=target_height, mask='auto')
    elif index == 4:
        c.drawString(200, 710, f"{anagrafica.cognome} {anagrafica.nome}")

        c.drawString(120, 681, anagrafica.luogo)
        c.drawString(220, 681, f"{anagrafica.giorno}/{anagrafica.mese}/{anagrafica.anno}")
        c.drawString(400, 681, residenza.citta)

        c.drawString(100, 655, residenza.via)
        c.drawString(340, 655, residenza.num_civ)
        c.drawString(440, 655, residenza.cap)

        c.drawString(180, 626, anagrafica.codfisc)

        c.drawString(60, 584, datetime.now().strftime("%d/%m/%Y"))

        c.drawString(57, 515, "X")

        c.drawString(100, 90, datetime.now().strftime("%d/%m/%Y"))
        target_width = 90
        target_height = (target_width / orig_width) * orig_height
        c.drawImage(signature, 360, 70, width=target_width, height=target_height, mask='auto')

    c.save()
    buffer.seek(0)
    return buffer

def second_overlay_pdf(data, index):
    buffer = BytesIO()
    c = canvas.Canvas(buffer)

    signature = ImageReader(str(SIGNATURE_PATH))
    orig_width, orig_height = signature.getSize()
        
    if index == 3:
        print("signature")
        target_width = 90
        target_height = (target_width / orig_width) * orig_height
        c.drawImage(signature, 55, 200, width=target_width, height=target_height, mask='auto')
    
    c.save()
    buffer.seek(0)
    return buffer

def editor(data, pdf_name = ["1) PREASSUNTIVI AUTONOMI OCCASIONALI.pdf", "757_PDFsam_12052025_AUT.pdf"]):
    
    for j in range(2):
        input_path = INPUT_DIR / pdf_name[j]
        output_path = OUTPUT_DIR / pdf_name[j]

        reader = PdfReader(input_path)
        writer = PdfWriter()
        for i, page in enumerate(reader.pages):
            if j == 0:
                overlay_data = first_overlay_pdf(data, i)
            elif j == 1:
                overlay_data = second_overlay_pdf(data, i)

            if overlay_data is None:
                writer.add_page(page)  # nessuna modifica
                continue

            overlay_pdf = PdfReader(overlay_data)
            if not overlay_pdf.pages:
                writer.add_page(page)  # fallback sicurezza
                continue

            overlay_page = overlay_pdf.pages[0]
            page.merge_page(overlay_page)
            writer.add_page(page)

        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        with open(output_path, "wb") as f:
            writer.write(f)
        print(f"PDF compilato salvato come: {output_path}")


