## minimal working example
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
