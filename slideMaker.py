import os,sys,commands

source = ""

header = """
\\documentclass{beamer}
\\usepackage[absolute,overlay]{textpos}
\\usepackage{graphicx}
\\usepackage{xcolor}
\\usepackage{slashed}
\\setbeamertemplate{navigation symbols}{}
\\usetheme{AnnArbor}
\\usecolortheme{dolphin}
\\setbeamercolor*{frametitle}{fg=blue!70!yellow,bg=blue!70!black!10,series=\\bfseries}
\\setbeamercolor{title}{fg=white,bg=blue!70!yellow,series=\\bfseries}
\\setbeamertemplate{headline}{} % suppress that top bar
\\useinnertheme{rectangles}
% \\setbeamertemplate{frametitle}[default][center]
% \\usepackage{dejavu}

\\newcommand{\\point}[1]{ \\begin{itemize} \\item{#1} \\end{itemize} }
\\newcommand{\\subpoint}[1]{ \\begin{itemize} \\item[] \\begin{itemize} \\item{#1} \\end{itemize} \\end{itemize} }
\\newcommand{\\met}{\\slashed{E}_T}
\\newcommand{\\red}[1]{\\textcolor{red}{#1}}
\\newcommand{\\blue}[1]{\\textcolor{blue}{#1}}
\\newcommand{\\orange}[1]{\\textcolor{orange}{#1}}

\\begin{document}
\\author[AUTHORHERE]{}
\\date{\\today} 
\\institute[SNT] 
{
    \\begin{center}
    N. Amin, C. Campagnari, A. George, F. Golf, J. Gran,\\\\ B. Marsh, I. Suarez, S. Wang\\\\ (UCSB)\\\\ \\vspace{0.3cm} 
    G. Cerati, M. Derdzinski, D. Klein, D. Olivito, G. Zevi Della Porta, \\\\ C. Welke, J. Wood, F. W\\"urthwein, A. Yagil \\\\ (UCSD)\\\\ \\vspace{0.3cm} 
        L. Bauerdick, K. Burkett, O. Gutsche, S. Jindariani, \\\\ J. Linacre, M. Liu, R. Lopes de Sa, H. Weber  \\\\ (FNAL) \\\\ 
        \\end{center}
}
\\addtobeamertemplate{frametitle}{}{%
    \\begin{textblock*}{2.1cm}(0.80\\textwidth,0.08cm)
        \\includegraphics[height=0.82cm]{ucsbwave.pdf}
    \\end{textblock*}
    \\begin{textblock*}{2.1cm}(0.98\\textwidth,0.09cm)
        \\includegraphics[height=0.82cm]{cmsbwlogothick.png}
    \\end{textblock*}
} \n\n
"""

footer = "\\end{document}"

def bulletsToCode(bullets):
    code = ""
    for bullet in bullets:
        if(len(bullet) < 4): continue
        if(bullet.strip().startswith("--")):
            code += "\\subpoint{%s} \n" % (bullet.replace("--","",1).strip())
        else:
            code += "\\point{%s} \n" % (bullet.replace("-","",1).strip())
    return code

def bulletLength(text,subpoint=False):
    text = text.replace("\\","@")
    text = text.replace("\\\\","@")
    cleanwords = []
    for word in text.split():
        if("@" in word):
            if("{" in word and "}" in word):
                word = word.replace("}","").split("{")[-1]
                pass
            else:
                word = "XXX"
        cleanwords.append(word)

    cleanline = " ".join(cleanwords)

    length = len(cleanline)+5*subpoint
    return length

def bulletNLines(bullets):
    nlines = 0
    for bullet in bullets:
        if(len(bullet) < 4): continue
        nlines += bulletLength(bullet)//71 + 1
    return nlines


def textLinesToPlotHeight(nlines):
    return 0.86 - nlines*0.05

def addSlideTitle(title):
    code = """
    \\title{%s}
    \\begin{frame}
    \\titlepage
        \\begin{textblock*}{2.1cm}(0.12\\textwidth,0.8\\textheight)
            \\includegraphics[height=1.3cm]{ucsbwave.pdf}
        \\end{textblock*}
        \\begin{textblock*}{2.1cm}(0.8\\textwidth,0.8\\textheight)
            \\includegraphics[height=1.3cm]{cmsbwlogothick.png}
        \\end{textblock*}
    \\end{frame} \n\n
    """ % (title)
    return code


def addSlidePlot(slideTitle, plotName):
    code = """
    \\begin{frame}\\frametitle{%s}
    \\begin{center}
    \\vspace*{-0.035\\textheight}\\includegraphics[height=0.88\\textheight,keepaspectratio]{%s}
    \\end{center}
    \\end{frame} \n\n
    """ % (slideTitle, plotName)
    return code

def addSlidePlotPlot(slideTitle, plotName1, plotName2):
    code = """
    \\begin{frame}\\frametitle{%s}
    \\begin{center}
    \\vspace*{-0.035\\textheight}\\includegraphics[height=0.95\\textheight,width=0.48\\textwidth,keepaspectratio]{%s} \\hfill
    \\vspace*{-0.035\\textheight}\\includegraphics[height=0.95\\textheight,width=0.48\\textwidth,keepaspectratio]{%s}
    \\end{center}
    \\end{frame} \n\n
    """ % (slideTitle, plotName1, plotName2)
    return code

def addSlideText(slideTitle,bullets):
    code = "\\begin{frame}\\frametitle{%s}\\begin{itemize} \n" % (slideTitle)
    code += bulletsToCode(bullets)
    code += "\\end{itemize}\\end{frame} \n\n"
    return code

def addSlideTextPlot(slideTitle,bullets,plotName):
    code = "\\begin{frame}\\frametitle{%s}\\begin{itemize} \n" % (slideTitle)
    code += bulletsToCode(bullets)
    code += "\\centering"
    code += "\\vspace*{-0.035\\textheight}\\includegraphics[height=%.2f\\textheight,keepaspectratio]{%s} \n" \
                % (textLinesToPlotHeight(bulletNLines(bullets)),plotName)
    code += "\\end{itemize}\\end{frame} \n\n" 
    return code

def addSlideTextPlotPlot(slideTitle,bullets,plotName1,plotName2):
    code = "\\begin{frame}\\frametitle{%s}\\begin{itemize} \n" % (slideTitle)
    code += bulletsToCode(bullets)
    code += "\\centering"
    code += "\\vspace*{-0.035\\textheight}\\includegraphics[height=%.2f\\textheight,width=0.48\\textwidth,keepaspectratio]{%s} \n" \
                % (textLinesToPlotHeight(bulletNLines(bullets)),plotName1)
    code += "\\vspace*{-0.035\\textheight}\\includegraphics[height=%.2f\\textheight,width=0.48\\textwidth,keepaspectratio]{%s} \n"  \
                % (textLinesToPlotHeight(bulletNLines(bullets)),plotName2)
    code += "\\end{itemize}\\end{frame} \n\n" 
    return code



content = """
- first \\textbf{bullet} point and if I make it long enough, it should wrap to the next line
 -- first secondary bullet \\textcolor{blue}{point} similarly this should wrap to the next line given enough length
 - lorem ipsum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed   
 -- tempor incididunt ut labore et dolore magna aliqua. Ut enim ad mini aa 
 -- second secondary bullet point $\\met$
 -- third secondary bullet \\orange{test}
second \\textcolor{red}{point}
third bullet point
 -- fourth secondary bullet point $Z\\rightarrow\\mu\\mu$
 -- fourth secondary bullet point $Z \\rightarrow \\mu\\mu$
"""
bullets = content.split("\n")
content2 = "\n".join(bullets[0:4])


def addSlide(title=None,text=None,p1=None,p2=None):
    global source

    bullets = []
    if( text ): bullets = text.split("\n")

    if( not title ):
        if( p1 and not p2 ): title = p1.replace("_","\\_").split(".")[0].split("/")[-1]
        elif( p2 and not p1 ): title = p1.replace("_","\\_").split(".")[0].split("/")[-1]
        elif( p1 and p2 ):
            title = p1.replace("_","\\_").split(".")[0].split("/")[-1] + ", " \
                  + p2.replace("_","\\_").split(".")[0].split("/")[-1]
        else: title = "\\phantom{}"

    if( p1 and p2 ):
        if( text ):
            print ">>> Adding TextPlotPlot slide"
            source += addSlideTextPlotPlot(title,bullets,p1,p2)
        else:
            print ">>> Adding PlotPlot slide"
            source += addSlidePlotPlot(title,p1,p2)
    elif( p1 ):
        if( text ):
            print ">>> Adding TextPlot slide"
            source += addSlideTextPlot(title,bullets,p1)
        else:
            print ">>> Adding Plot slide"
            source += addSlidePlot(title,p1)
    elif( text ):
        print ">>> Adding Text slide"
        source += addSlideText(title,bullets)
    elif( title ):
        print ">>> Adding Title slide"
        source += addSlideTitle(title)
    else:
        print "couldn't figure out what you want"

def initSlides(name="Nick"):
    global source, header
    if("Nick" in name): 
        header = header.replace("N. Amin", "\\textbf{N. Amin}")
        header = header.replace("AUTHORHERE", "Nick Amin")
    elif("Sicheng" in name): 
        header = header.replace("S. Wang", "\\textbf{S. Wang}")
        header = header.replace("AUTHORHERE", "Sicheng Wang")
    elif("Alex" in name): 
        header = header.replace("A. George", "\\textbf{A. George}")
        header = header.replace("AUTHORHERE", "Alex George")
    else:
        print "who are you?"
    source += header
    print ">>> Initializing slides"

def writeSlides(output="output.tex", compile=False):
    global source
    source += footer
    fh = open(output,"w")
    fh.write(source)
    fh.close()
    print ">>> Wrote slides"

    if(compile):
        stat,out = commands.getstatusoutput("pdflatex -interaction=nonstopmode %s" % output)
        if(stat not in [0, 256]): # 256 is warnings and 0 is good
            print ">>> ERROR: Tried to compile, but failed with status %i. Last few lines of printout below." % stat
            print "_"*40
            print "\n".join(out.split("\n")[-15:])
        else:
            print ">>> Compiled slides to", output.replace(".tex",".pdf")

if __name__ == '__main__':
    content = """
    - first \\textbf{bullet} point and if I make it long enough, it should wrap to the next line
     -- first secondary bullet \\textcolor{blue}{point} similarly this should wrap to the next line given enough length
     - lorem ipsum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed   
     -- tempor incididunt ut labore et dolore magna aliqua. Ut enim ad mini aa 
     -- second secondary bullet point $\\met$
     -- third secondary bullet \\orange{test}
    second \\textcolor{red}{point}
    third bullet point
     -- fourth secondary bullet point $Z\\rightarrow\\mu\\mu$
     -- fourth secondary bullet point $Z \\rightarrow \\mu\\mu$
    """
    bullets = content.split("\n")
    content2 = "\n".join(bullets[0:4])

    initSlides("Nick")
    addSlide(title="this is where I put a title")
    addSlide(p1="./test/yields.pdf",p2="./test/yields.pdf")
    addSlide(p1="./test/zmass.pdf")
    addSlide(text=content)
    addSlide(text=content2, p1="./test/zmass.pdf")
    addSlide(text=content2, p1="./test/filt.pdf")
    addSlide(text=content2, p1="./test/zmass.pdf", p2="./test/zmass.pdf")
    writeSlides("test.tex", compile=True)

