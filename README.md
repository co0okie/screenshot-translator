create a file `config.py` first  
example config.py:  
```python
SCREENSHOT_DIRECTORY = r'C:\Users\hank\Pictures\Screenshots'

# the location of the tesseract executable
# install tesseract from https://tesseract-ocr.github.io/tessdoc/Installation.html
PYTESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Get api key from https://platform.openai.com/docs/overview
OPENAI_API_KEY = r'<your api key>'
```