from docx import Document
from docx.shared import Pt

#Abre Arquivo Word
arquivoWord = Document("Certificado1.docx")

#Seleciona o estilo
estilo = arquivoWord.styles["Normal"]

for paragrafo in arquivoWord.paragraphs:

    if "@nome" in paragrafo.text:
        paragrafo.text = "João Pedro Silva"
        fonte = estilo.font
        fonte.name = "Calibri (Corpo)"
        fonte.size = Pt(24)

#Salvando o arquivo
arquivoWord.save("João Pedro Silva.docx")