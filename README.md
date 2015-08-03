## minimal minimal minimal working example
1) check out repo and make sure there's a folder called "dump" inside the public_html directory

2) python slideMaker.py

3) look at the output

This makes it easy to edit the slideMaker and test it on-the-fly.

## standalone minimal working example
Inside the main repository directory, create and execute a python file with the contents
```python
import slideMaker as sm

content = """
 - first \\textbf{bullet} \\red{point} and if I make it long enough, it should wrap to the next line
   -- first secondary bullet \\textcolor{blue}{point}. similarly this should wrap to the next line given enough length
   -- second secondary bullet point $\\met$
   -- third secondary bullet \\orange{test}
"""

t1 = sm.textObject(x=0.25,y=0.15,width=0.3, text="testlabel", color="red", size=0, bold=False) 
t2 = sm.textObject(x=0.75,y=0.15,width=0.3, text="testlabel", color="coolblue", size=0, bold=False) 

# supported themes are "nick", "alex", and "madrid"
for t in ["nick","alex","madrid"]:
    # test2 and test3 can be folders with your plots, so you can execute this script anywhere really
    # themecolor takes RGB. could put in explicit color names, but RGB more robust
    sm.initSlides(me="Nick",themeName=t,opts="--graphicspaths ./test2/,./test3/ --themecolor 51,51,179")
    sm.addSlide(title="this is where I'd put a title if I had one that was long", opts="--shorttitle shorter title")

    # pass in a list of textobjects (which are just dicts, so they can be modified too)
    sm.addSlide(p1="yields.pdf",p2="yields.pdf", textobjects=[t1,t2])
    sm.addSlide(p1="test/yields.pdf",p2="test/yields.pdf")
    sm.addSlide(p1="test/zmass.pdf")
    sm.addSlide(text=content+content)

    # slides reset their numbering when you start the backup section
    sm.startBackup()
    sm.addSlide(text=content, p1="test/filt.pdf", opts="--sidebyside")
    sm.addSlide(text=content, p1="test/zmass.pdf", p2="test/zmass.pdf")
    sm.writeSlides("test_%s.tex" % t, opts="--compile --copy")
```
This will produce test_*.pdf with an example slide for each of the possible slide types, and copy them to your public_html folder

## Notes:
* put updated style files into style and include them in a way similar to enumitem

## TODO:
* figure out good algorithm for resizing images so that they don't overlap with text
** see http://www.latex-community.org/forum/viewtopic.php?f=45&t=22655
* option for arrows
