# Nombre de los archivos de Markdown y PDFs
MD_FILES  = OneShot01\ El\ pueblo\ sin\ nombre.md
PDF_FILE = oneshot01.pdf

# Opciones para Pandoc
PANDOC_ENGINE = --pdf-engine=xelatex
PANDOC_OPTIONS = -V papersize=a4 -V geometry:margin=1.5cm

# Regla para generar el PDF específico
.PHONY: oneshot01 clean

oneshot01: $(PDF_FILE)

oneshot01.pdf: $(MD_FILES)
	pandoc $(PANDOC_ENGINE) $(PANDOC_OPTIONS) "$<" -o "$@"

# Limpiar PDFs generados
clean:
	rm -f $(PDF_FILE)
