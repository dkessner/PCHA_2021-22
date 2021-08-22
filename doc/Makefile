#
# Makefile
#

# $* stem of implicit rule match 
# $@ target 
# $< first prerequisite


pdf_targets = $(patsubst %.md,%.pdf,$(wildcard *.md))

html_targets = $(patsubst %.md,%.html,$(wildcard *.md))

targets = $(pdf_targets) $(html_targets)

all: $(targets)
	@echo Targets: $(targets)

# --mathjax: currently uses MathJax CDN for rendering
# -s: standalone (use full HTML template)
# -H / --include-in-header: include HTML file

%.html: %.md
	pandoc $< -o $@ -t html5 -s --mathjax -H tables.html

%.pdf: %.md
	pandoc $< -o $@ 

clean:
	rm -f $(targets)


