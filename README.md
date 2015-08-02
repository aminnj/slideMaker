## minimal minimal minimal working example
1) check out repo

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

# supported themes are "nick", "alex", and "madrid"
sm.initSlides(me="Nick",themeName="nick")
sm.addSlide(title="this is where I put a title")
sm.addSlide(p1="test/yields.pdf",p2="test/yields.pdf")
sm.addSlide(p1="test/zmass.pdf")
sm.addSlide(text=content+content)
sm.addSlide(text=content, p1="test/filt.pdf")
sm.addSlide(text=content, p1="test/zmass.pdf", p2="test/zmass.pdf")
sm.writeSlides("test.tex", compile=True, copy=True)
```
This will produce test.pdf with an example slide for each of the possible slide types, and copy this to your public_html folder

## Notes:
* remember to compile twice to pick up the proper slide numbers (stupid latex)
* put updated style files into style and include them in a way similar to enumitem

## TODO:
* add slide type that has text on the left, picture on the right
* add option parser
** already made (but not implemented) in utils.py
** move some utility functions (like the bullet stuff) into utils.py to unclutter slideMaker.py
* figure out good algorithm for resizing images so that they don't overlap with text
** see http://www.latex-community.org/forum/viewtopic.php?f=45&t=22655
* option to add folder to graphicspath
* option for free floating text
