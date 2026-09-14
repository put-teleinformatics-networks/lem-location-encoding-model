# Wymusza pdfLaTeX i pelny cykl z BibTeX (LaTeX -> BibTeX -> LaTeX x2).
# Overleaf oraz lokalne `latexmk -pdf` respektuja te ustawienia.
$pdf_mode = 1;          # 1 = pdflatex
$bibtex_use = 2;        # zawsze uruchamiaj bibtex, gdy jest .bib
$out_dir = '.';
