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
 - second primary bullet point $Z \\rightarrow \\mu\\mu$
"""

sm.initSlides("Nick")
sm.addSlide(title="this is where I put a title")
sm.addSlide(p1="test/yields.pdf",p2="test/yields.pdf")
sm.addSlide(p1="test/zmass.pdf")
sm.addSlide(text=content+content)
sm.addSlide(text=content, p1="test/filt.pdf")
sm.addSlide(text=content, p1="test/zmass.pdf", p2="test/zmass.pdf")
sm.writeSlides("test.tex", compile=True)
```
This will produce test.pdf with an example slide for each of the possible slide types.


## TODO:
* support Madrid theme in Software/SlideMaker
* support minimal ("Alex") theme in Software/SlideMaker
    ** custom first slide, blank theme, tikz triangle page number
* if all entries are bullets, bullets should not be indented as this wastes space
* add slide type that has text on the left, picture on the right
* if a slide has a small amount of text, have an option to have text start at top of slide right under the title
* add option parser
* handle long titles properly
* figure out good algorithm for resizing images so that they don't overlap with text
