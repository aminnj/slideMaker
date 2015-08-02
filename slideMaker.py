import os,sys,commands
import utils
from strings import *

source = ""
theme = ""

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
        source = source.replace("TITLEHERE",utils.splitTitle(title))
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
    code += utils.bulletsToCode(bullets)
    code += "\\end{frame} \n\n"
    return code

def addSlideTextPlot(slideTitle,bullets,plotName):
    code = "\\begin{frame}\\frametitle{%s} \n" % (slideTitle)
    code += utils.bulletsToCode(bullets)
    code += "\\begin{center}"
    code += "\\includegraphics[height=%.2f\\textheight,keepaspectratio]{%s} \n" \
                % (utils.textLinesToPlotHeight(utils.bulletNLines(bullets)),plotName)
    code += "\\end{center}\\end{frame} \n\n" 
    return code

def addSlideTextPlotPlot(slideTitle,bullets,plotName1,plotName2):
    code = "\\begin{frame}\\frametitle{%s} \n" % (slideTitle)
    code += utils.bulletsToCode(bullets)
    code += "\\begin{center}"
    code += "\\includegraphics[height=%.2f\\textheight,width=0.48\\textwidth,keepaspectratio]{%s} \n" \
                % (utils.textLinesToPlotHeight(utils.bulletNLines(bullets)),plotName1)
    code += "\\includegraphics[height=%.2f\\textheight,width=0.48\\textwidth,keepaspectratio]{%s} \n"  \
                % (utils.textLinesToPlotHeight(utils.bulletNLines(bullets)),plotName2)
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
    source = ""
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

def writeSlides(output="output.tex", opts="--compile"):
    global source
    source += footer
    fh = open(output,"w")
    fh.write(source)
    fh.close()
    print ">>> Wrote slides"

    opts = utils.parseOptions(opts)

    if(opts["compile"]):
        # compile twice to get correct slide numbers. latex is dumb. is this the only way?
        stat,out = commands.getstatusoutput("pdflatex -interaction=nonstopmode %s && \
                                             pdflatex -interaction=nonstopmode %s " % (output,output) )
        if("Fatal error" in out):
            print ">>> ERROR: Tried to compile, but failed. Last few lines of printout below."
            print "_"*40
            print "\n".join(out.split("\n")[-30:])
            return
        else:
            print ">>> Compiled slides to", output.replace(".tex",".pdf")

        if(opts["copy"]):
            stat,out = commands.getstatusoutput("cp %s ~/public_html/%s/" % (output.replace(".tex",".pdf"), "dump" if opts["dump"] else ""))
            print ">>> Copied output to uaf-6.t2.ucsd.edu/~%s/%s%s" % (os.getenv("USER"), "dump/" if opts["dump"] else "", output.replace(".tex",".pdf"))

def startBackup():
    global source
    color = "black"
    if(theme == "alex"): color = "alexcolor"
    if(theme == "nick"): color = "nickcolor"
    if(theme == "madrid"): color = "madridcolor"

    source += """
    \\appendix
    \\begin{frame}[plain]
    \\centering
    \\begin{textblock*}{10cm}[0.0,0.0](5.5cm,4.0cm)
    \\begin{LARGE} \\textcolor{%s}{\\textbf{Backup}} \\end{LARGE}
    \\end{textblock*}
    \\end{frame}
    """ % (color)


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


    for t in ["nick", "alex", "madrid"]:
    # for t in ["nick"]:
        initSlides(me="Nick",themeName=t)
        addSlide(title="this is where I put a long title")
        addSlide(p1="yields.pdf",p2="yields.pdf")
        addSlide(p1="zmass.pdf")
        addSlide(text=content)
        addSlide(text=content2, p1="zmass.pdf")
        startBackup()
        addSlide(text=content2, p1="filt.pdf")
        addSlide(text=content2, p1="zmass.pdf", p2="zmass.pdf")
        writeSlides("test_%s.tex" % t, opts="--compile --copy --dump")

