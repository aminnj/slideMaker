import os,sys,commands

source = ""

institute = """
    N. Amin, C. Campagnari, A. George, F. Golf, J. Gran,\\\\ B. Marsh, I. Suarez, S. Wang\\\\ (UCSB)\\\\ \\vspace{0.3cm} 
    G. Cerati, M. Derdzinski, D. Klein, D. Olivito, G. Zevi Della Porta, \\\\ C. Welke, J. Wood, F. W\\"urthwein, A. Yagil \\\\ (UCSD)\\\\ \\vspace{0.3cm} 
        L. Bauerdick, K. Burkett, O. Gutsche, S. Jindariani, \\\\ J. Linacre, M. Liu, R. Lopes de Sa, H. Weber  \\\\ (FNAL) \\\\ 
"""

commonHeader = """
\\documentclass[aspectratio=1610]{beamer}
\\usepackage[absolute,overlay]{textpos}
\\usepackage{tikz}
\\usepackage{microtype}
\\usepackage{graphicx}
\\usepackage{xcolor}
\\usepackage{slashed}
\\usepackage{amssymb}
\\graphicspath{ {./test/}, {./logos/} }
\\setbeamertemplate{navigation symbols}{}

\\newcommand{\\met}{\\slashed{E}_T}
\\newcommand{\\red}[1]{\\textcolor{red}{#1}}
\\newcommand{\\blue}[1]{\\textcolor{blue}{#1}}
\\newcommand{\\orange}[1]{\\textcolor{orange}{#1}}

\\definecolor{darkgreen}{RGB}{0,100,0}
\\definecolor{gray}{RGB}{128,128,128}
\\definecolor{grey}{RGB}{128,128,128}
\\definecolor{coolblue}{RGB}{51,51,179}
\\definecolor{alexcolor}{RGB}{51,51,179}

\\author[AUTHORHERE]{}
\\date{\\today} 
\\institute[SNT] 
{
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
\\setlist[itemize]{label=$\\textcolor{coolblue}{\\blacktriangleright}$,leftmargin=*}

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
\\setlist[itemize]{label=$\\textcolor{coolblue}{\\blacktriangleright}$,leftmargin=*}

\\begin{document}
"""

footer = "\\end{document}"

def bulletsToCode(bullets):
    code = "\\begin{itemize}\n"
    wasSubpoint=False
    bullets = [bullet.strip() for bullet in bullets if len(bullet.strip()) > 3]
    for i,bullet in enumerate(bullets):
        isSubpoint = bullet.strip().startswith("--")
        isLast = i == (len(bullets)-1)
        bullet = bullet.replace("--","",1).replace("-","",1).strip()

        if(isSubpoint and not wasSubpoint):
            code += "    \\begin{itemize}\n"
            code += "      \\item %s \n" % (bullet)
        elif(wasSubpoint and not isSubpoint):
            code += "    \\end{itemize}\n"
            code += "  \\item %s \n" % (bullet)
        elif(wasSubpoint and isSubpoint):
            code += "      \\item %s \n" % (bullet)
        elif(not wasSubpoint and not isSubpoint):
            code += "  \\item %s \n" % (bullet)
        else: print "You goofed with your logic"

        if(isLast and isSubpoint): code += "  \\end{itemize}\n"

        wasSubpoint = isSubpoint

    code += "\\end{itemize}\n"
    return code

def cleanTex(text):
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
    return " ".join(cleanwords)

def bulletLength(text,subpoint=False):
    cleanline = cleanTex(text)
    return len(cleanline)+5*subpoint

def bulletNLines(bullets):
    nlines = 0
    for bullet in bullets:
        if(len(bullet) < 4): continue
        nlines += bulletLength(bullet)//71 + 1
    return nlines

def textLinesToPlotHeight(nlines):
    return 0.85 - nlines*0.05

def splitTitle(title):
    # title = cleanTex(title) # this removes the tex from the title!
    if(len(title) <= 20):
        return "\\\\ \\vspace{0.4cm} "+title
    else:
        return title[:20]+title[20:].split()[0] + "\\\\ \\vspace{0.4cm}" + " ".join(title[20:].split()[1:])

def addSlideTitle(title):
    global source

    titlePageNick = """
    \\title{%s}
    \\begin{frame}
    \\titlepage
        \\begin{textblock*}{2.1cm}(0.12\\textwidth,0.8\\textheight)
            \\includegraphics[height=1.3cm]{./logos/ucsbwave.pdf}
        \\end{textblock*}
        \\begin{textblock*}{2.1cm}(0.8\\textwidth,0.8\\textheight)
            \\includegraphics[height=1.3cm]{./logos/cmsbwlogothick.png}
        \\end{textblock*}
    \\end{frame} \n\n
    """ % (title)

    titlePageAlex = """
    \\frame[plain]{ \\titlepage }

    \\usebackgroundtemplate{
    \\begin{tikzpicture}[thick]
    \\draw[fill=alexcolor, draw=alexcolor](0cm,0.0cm) -- (21.3cm,0.0cm) -- (21.3cm,21.3cm) -- (0.0cm,0.0cm);
    \\end{tikzpicture}
    }
    """

    titlePageMadrid = """
    \\title{%s}
    \\begin{frame}
    \\titlepage
        \\begin{textblock*}{2.1cm}(0.12\\textwidth,0.8\\textheight)
            \\includegraphics[height=1.3cm]{./logos/ucsbwave.pdf}
        \\end{textblock*}
        \\begin{textblock*}{2.1cm}(0.8\\textwidth,0.8\\textheight)
            \\includegraphics[height=1.3cm]{./logos/cmsbwlogothick.png}
        \\end{textblock*}
    \\end{frame} \n\n
    """ % (title)

    if(theme == "nick"):
        source += titlePageNick
    elif(theme == "alex"):
        source = source.replace("TITLEHERE",splitTitle(title))
        source += titlePageAlex
    elif(theme == "madrid"):
        source += titlePageMadrid
    else:
        source += "\\frame{ \\titlepage }"


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
    code = "\\begin{frame}\\frametitle{%s} \n" % (slideTitle)
    code += bulletsToCode(bullets)
    code += "\\end{frame} \n\n"
    return code

def addSlideTextPlot(slideTitle,bullets,plotName):
    code = "\\begin{frame}\\frametitle{%s} \n" % (slideTitle)
    code += bulletsToCode(bullets)
    code += "\\begin{center}"
    code += "\\includegraphics[height=%.2f\\textheight,keepaspectratio]{%s} \n" \
                % (textLinesToPlotHeight(bulletNLines(bullets)),plotName)
    code += "\\end{center}\\end{frame} \n\n" 
    return code

def addSlideTextPlotPlot(slideTitle,bullets,plotName1,plotName2):
    code = "\\begin{frame}\\frametitle{%s} \n" % (slideTitle)
    code += bulletsToCode(bullets)
    code += "\\begin{center}"
    code += "\\includegraphics[height=%.2f\\textheight,width=0.48\\textwidth,keepaspectratio]{%s} \n" \
                % (textLinesToPlotHeight(bulletNLines(bullets)),plotName1)
    code += "\\includegraphics[height=%.2f\\textheight,width=0.48\\textwidth,keepaspectratio]{%s} \n"  \
                % (textLinesToPlotHeight(bulletNLines(bullets)),plotName2)
    code += "\\end{center}\\end{frame} \n\n" 
    return code



def addSlide(title=None,text=None,p1=None,p2=None):
    global source

    bullets = []
    if( text ): bullets = text.split("\n")

    if( not title ):
        cleanP1 = p1.replace("_","\\_").rsplit(".",1)[0].split("/")[-1] if p1 else ""
        cleanP2 = p2.replace("_","\\_").rsplit(".",1)[0].split("/")[-1] if p2 else ""
        if( p1 and not p2 ): title = cleanP1
        elif( p2 and not p1 ): title = cleanP2
        elif( p1 and p2 ): title = cleanP1 + ", " + cleanP2
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
        addSlideTitle(title)
    else:
        print "couldn't figure out what you want"

def initSlides(me="Nick", themeName="nick"):
    global source, commonHeader, theme, themeAlex
    theme = themeName.lower()
    print ">>> Hi",me
    print ">>> Using theme:",theme

    source += commonHeader
    if(theme == "nick"):
        source += themeNick
    elif(theme == "alex"):
        source += themeAlex
    elif(theme == "madrid"):
        source += themeMadrid
    else:
        print "unsupported theme:", theme
    

    if("Nick" in me): 
        source = source.replace("AUTHORHERE", "Nick Amin")
        source = source.replace("N. Amin", "\\underline{\\textbf{N. Amin}}")
    elif("Sicheng" in me): 
        source = source.replace("AUTHORHERE", "Sicheng Wang")
        source = source.replace("S. Wang", "\\underline{\\textbf{S. Wang}}")
    elif("Alex" in me): 
        source = source.replace("AUTHORHERE", "Alex George")
        source = source.replace("A. George", "\\underline{\\textbf{A. George}}")
    else:
        print "who are you?"

    print ">>> Initializing slides"

def writeSlides(output="output.tex", compile=False, copy=False, dump=False):
    global source
    source += footer
    fh = open(output,"w")
    fh.write(source)
    fh.close()
    print ">>> Wrote slides"

    if(compile):
        stat,out = commands.getstatusoutput("pdflatex -interaction=nonstopmode %s" % output)
        if("Fatal error" in out):
            print ">>> ERROR: Tried to compile, but failed. Last few lines of printout below."
            print "_"*40
            print "\n".join(out.split("\n")[-30:])
            return
        else:
            print ">>> Compiled slides to", output.replace(".tex",".pdf")

        if(copy):
            stat,out = commands.getstatusoutput("cp %s ~/public_html/%s/; echo $USER" % (output.replace(".tex",".pdf"), "dump" if dump else ""))
            user = out.split("\n")[-1].strip()
            print ">>> Copied output to uaf-6.t2.ucsd.edu/~%s/%s%s" % (user, "dump/" if dump else "", output.replace(".tex",".pdf"))


if __name__ == '__main__':
    content = """
     - first \\textbf{bullet} point and if I make it long enough, it should wrap to the next line
     -- first secondary bullet \\textcolor{blue}{point} similarly this should wrap to the next line given enough length
     - lorem ipsum Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed   
     -- tempor incididunt ut labore et dolore magna aliqua. Ut enim ad mini aa 
     -- second secondary bullet point $\\met$
     -- third secondary bullet \\orange{test}
     - second \\textcolor{red}{point}
     - third bullet point
     -- fourth secondary bullet point $Z\\rightarrow\\mu\\mu$
     -- fourth secondary bullet point $Z \\rightarrow \\mu\\mu$
    """
    bullets = content.split("\n")
    content2 = "\n".join(bullets[0:4])


    initSlides(me="Nick",themeName="madrid")
    addSlide(title="this is where I put a long title")
    addSlide(p1="yields.pdf",p2="yields.pdf")
    addSlide(p1="zmass.pdf")
    addSlide(text=content)
    addSlide(text=content2, p1="zmass.pdf")
    addSlide(text=content2, p1="filt.pdf")
    addSlide(text=content2, p1="zmass.pdf", p2="zmass.pdf")
    writeSlides("test.tex", compile=True, copy=True, dump=True)

