all: main.tex
	xelatex -shell-escape main.tex
	texindy -M lang/korean/utf8-lang main.idx
	sed -i '' -r 's/\\textbf{([0-9]+)}/\\textbf{\\hyperpage{\1}}/g' main.ind
	xelatex -shell-escape main.tex

.PHONY: clean
clean:
	rm -rf _minted-main *.aux *.idx *.ilg *.ind *.log *.out *.pdf *.toc
