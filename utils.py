### utility functions that don't directly touch the latex source go here


listOfOptions = ["dump", "copy", "compile", "graphicspaths", "shorttitle", "themecolor"]
def parseOptions(optString):
    opts = { }
    for optName in listOfOptions:
        opts[optName] = False

    for opt in optString.split("--"):
        opt = opt.strip()
        if(len(opt.split()) < 1): continue
        optName = opt.split()[0].strip()
        if(optName not in listOfOptions): 
            print ">>> Warning: unrecognized option:",optName
            continue

        if(len(opt.split()) < 2):
            opts[optName] = True
        else:
            opts[optName] = " ".join(opt.split()[1:])

    return opts

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
    cutoff = 20
    if(len(title) <= cutoff):
        return "\\\\ \\vspace{0.4cm} "+title
    else:
        return title[:cutoff]+title[cutoff:].split()[0] + "\\\\ \\vspace{0.4cm}" + " ".join(title[cutoff:].split()[1:])


# print parseOptions("--dump --title left --caption this is stupid --unrecognizedopt")
