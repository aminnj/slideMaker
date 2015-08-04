### Long template strings go here

institute = """
    N. Amin, C. Campagnari, A. George, F. Golf, J. Gran,\\\\ B. Marsh, I. Suarez, S. Wang\\\\ (UCSB)\\\\ \\vspace{0.3cm} 
    G. Cerati, M. Derdzinski, D. Klein, D. Olivito, G. Zevi Della Porta, \\\\ C. Welke, J. Wood, F. W\\"urthwein, A. Yagil \\\\ (UCSD)\\\\ \\vspace{0.3cm} 
        L. Bauerdick, K. Burkett, O. Gutsche, S. Jindariani, \\\\ J. Linacre, M. Liu, R. Lopes de Sa, H. Weber  \\\\ (FNAL) \\\\ 
"""

commonHeader = """
%% \\documentclass[aspectratio=1610]{beamer}
\\documentclass{beamer}
\\usepackage[absolute,overlay]{textpos}
%% \\usepackage[absolute,overlay,showboxes]{textpos} %% showboxes for position debugging
\\usepackage{tikz}
\\usetikzlibrary{arrows,shapes}
\\usepackage{microtype}
\\usepackage{graphicx}
\\usepackage{xcolor}
\\usepackage{slashed}
\\usepackage{./styles/appendixnumberbeamer} 
\\usepackage{amssymb}
\\graphicspath{ GRAPHICSPATHHERE }
\\setbeamertemplate{navigation symbols}{}

\\newcommand{\\met}{\\slashed{E}_T}
\\newcommand{\\red}[1]{\\textcolor{red}{#1}}
\\newcommand{\\blue}[1]{\\textcolor{blue}{#1}}
\\newcommand{\\orange}[1]{\\textcolor{orange}{#1}}

\\definecolor{darkgreen}{RGB}{0,100,0}
\\definecolor{gray}{RGB}{128,128,128}
\\definecolor{grey}{RGB}{128,128,128}
\\definecolor{coolblue}{RGB}{51,51,179}
\\definecolor{nickcolor}{RGB}{51,51,179}
\\definecolor{alexcolor}{RGB}{0,0,255}
\\definecolor{madridcolor}{RGB}{51,51,179}

\\author[AUTHORHERE]{}
\\date{\\today} 
\\institute[SNT] 
{
    \\vspace*{-1cm}
    \\begin{center}
    %s
        \\end{center}
}

""" % (institute)

themeNick = """
\\usepackage{./styles/enumitem}
\\addtobeamertemplate{frametitle}{}{%
    \\begin{textblock*}{2.1cm}(0.80\\textwidth,0.08cm)
        \\includegraphics[height=0.82cm]{./logos/ucsbwave.pdf}
    \\end{textblock*}
    \\begin{textblock*}{2.1cm}(0.98\\textwidth,0.09cm)
        \\includegraphics[height=0.82cm]{./logos/cmsbwlogothick.png}
    \\end{textblock*}
} \n\n

\\usetheme{AnnArbor}
\\usecolortheme{dolphin}
\\setbeamercolor*{frametitle}{fg=blue!70!yellow,bg=blue!70!black!10}
\\setbeamercolor{title}{fg=white,bg=blue!70!yellow}
\\setbeamertemplate{headline}{} % suppress that top bar
\\useinnertheme{rectangles}
\\setlist[itemize]{label=$\\textcolor{nickcolor}{\\blacktriangleright}$,leftmargin=*}

\\begin{document}
"""

themeAlex = """
\\setbeamertemplate{footline}[frame number]
\\setbeamercolor{frametitle}{fg=alexcolor}
\\setbeamerfont{frametitle}{size=\\LARGE \\bfseries}
\\setbeamertemplate{footline}{\\raisebox{5pt}{\\makebox[\\paperwidth]{\\hfill\\makebox[10pt]{\\scriptsize\\textcolor{white}{\\insertframenumber\\hspace{2mm}}}}}}\\setbeamersize{text margin left=10pt,text margin right=10pt}

\\defbeamertemplate*{title page}{customized}[1][]{ 
  \\begin{textblock*}{12.8cm}(0cm,1.5cm)
  \\begin{center}
  \\usebeamerfont{title}
  \\textcolor{alexcolor}{\\textbf{\\huge TITLEHERE} } %% Allowed 20 characters upstairs and 30 downstairs
  \\end{center}
  \\end{textblock*}
  \\begin{center}
  \\textcolor{alexcolor}{\\rule{10cm}{2pt}}
  \\end{center}
  \\begin{textblock*}{12.8cm}(0cm,4.0cm)
  \\begin{center}
  %s
  \\end{center}
  \\end{textblock*}
  \\begin{textblock*}{2.7cm}(0cm, 0.1cm)
  \\includegraphics[width=2.7cm]{./logos/ucsb.pdf}
  \\end{textblock*}
  \\begin{textblock*}{2.2cm}(10.3cm, 0.2cm)
  \\includegraphics[width=2.2cm]{./logos/CMS.pdf}
  \\end{textblock*}
}

\\usebackgroundtemplate{
\\begin{tikzpicture}[thick]
\\draw[fill=alexcolor, draw=alexcolor](0cm,0.0cm) -- (21.3cm,0.0cm) -- (21.3cm,21.3cm) -- (0.0cm,0.0cm);
\\end{tikzpicture}
}

\\begin{document}
""" % (institute)

themeMadrid = """
\\usepackage{./styles/enumitem}
\\addtobeamertemplate{frametitle}{}{%
    \\begin{textblock*}{2.1cm}(0.80\\textwidth,0.08cm)
        \\includegraphics[height=0.82cm]{./logos/ucsbwave.pdf}
    \\end{textblock*}
    \\begin{textblock*}{2.1cm}(0.98\\textwidth,0.09cm)
        \\includegraphics[height=0.82cm]{./logos/cmsbwlogothick.png}
    \\end{textblock*}
} \n\n

\\usetheme{AnnArbor}
\\usecolortheme{wolverine}
\\setbeamertemplate{headline}{} % suppress that top bar
\\setlist[itemize]{label=$\\textcolor{madridcolor}{\\blacktriangleright}$,leftmargin=*}

\\begin{document}
"""

footer = "\\end{document}"
