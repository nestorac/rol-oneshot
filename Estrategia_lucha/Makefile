all:
#	pandoc La\ Torre\ del\ Estratega.md -o La\ Torre\ del\ Estratega.pdf --pdf-engine=xelatex -V geometry:"a4paper, margin=1.5cm" -V classoption=twocolumn --from markdown -V tables
#	pandoc La\ Torre\ del\ Estratega.md -o La\ Torre\ del\ Estratega.pdf --pdf-engine=xelatex -V geometry:"a4paper, margin=1.5cm" -V classoption=twocolumn --variable=longtable:false
#	pandoc La\ Torre\ del\ Estratega.md -o La\ Torre\ del\ Estratega.pdf --pdf-engine=xelatex -V geometry:"a4paper, margin=1.5cm"
#	pandoc La\ Torre\ del\ Estratega.md  -o La\ Torre\ del\ Estratega.pdf --pdf-engine=xelatex -V geometry:"a4paper, margin=1.5cm" -V classoption=twocolumn --template=notables.tex
	pandoc "La Torre del Estratega.md" \
  -o "La Torre del Estratega.pdf" \
  --pdf-engine=xelatex \
  -V geometry:"a4paper, margin=1.5cm" \
  -V classoption=twocolumn \
  --lua-filter=force-table.lua \
  --template=notables.tex
