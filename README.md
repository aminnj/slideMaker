## minimal working example
Inside the main repository directory, create and execute a python file with the contents
```python
from slideMaker import *

content = """
 - first \\textbf{bullet} \\red{point} and if I make it long enough, it should wrap to the next line
   -- first secondary bullet \\textcolor{blue}{point}. similarly this should wrap to the next line given enough length
   -- second secondary bullet point $\\met$
   -- third secondary bullet \\orange{test}
 - second primary bullet point $Z \\rightarrow \\mu\\mu$
"""

initSlides("Nick")
addSlide(title="this is where I put a title")
addSlide(p1="test/yields.pdf",p2="test/yields.pdf")
addSlide(p1="test/zmass.pdf")
addSlide(text=content+content)
addSlide(text=content2, p1="test/filt.pdf")
addSlide(text=content2, p1="test/zmass.pdf", p2="test/zmass.pdf")

writeSlides("test.tex", compile=True)
```
This will produce test.pdf with an example slide for each of the possible slide types.
