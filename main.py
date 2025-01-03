import glob
import os
import pytesseract
from chatGPT import ChatGPT
from scene import SceneRamune
from gui import GUI
import json
from config import PYTESSERACT_CMD, SCREENSHOT_DIRECTORY

scene = SceneRamune()

# install pytesseract
# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i
pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_CMD

def get_files(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    
def on_ocr():
    images = [f for f in get_files(SCREENSHOT_DIRECTORY) if f.startswith('螢幕擷取畫面')]
    images.sort(reverse=True)
    
    imagePath = os.path.join(SCREENSHOT_DIRECTORY, images[0])
    imagePath = scene.process_image(imagePath)
    
    # to get better model:
    # https://github.com/tesseract-ocr/tessdata/tree/main
    text = pytesseract.image_to_string(imagePath, lang='jpn')
    text = scene.process_orc_result(text)
    
    gui.set_input(text)

def on_go():
    text = gui.get_input()
    response = ChatGPT.chat(text)
    r = json.loads(response)
    response = f'{r['furigana']}\n{r['chinese']}\n{'\n'.join(map(lambda s: f'• {s}', r['detail']))}'
    gui.set_result(response)

if __name__ == '__main__':
    global gui
    gui = GUI(on_ocr, on_go)
    gui.start()