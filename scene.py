import os
import shutil
import cv2
import numpy as np

class Scene():
    @staticmethod
    def process_image(image_path: str) -> str:
        output_image_path = os.path.join(os.path.dirname(image_path), '.temp.screenshot-translator.png')
        shutil.copyfile(image_path, output_image_path)
        return output_image_path
    
    @staticmethod
    def process_orc_result(text: str) -> str:
        text = text.replace('\n', '').replace(' ', '')
        return text

class SceneWhiteText(Scene):
    @staticmethod
    def process_image(image_path: str):
        output_image_path = os.path.join(os.path.dirname(image_path), '.temp.screenshot-translator.png')
        shutil.copyfile(image_path, output_image_path)
        
        image = cv2.imread(output_image_path)
        
        # invert colors
        image = cv2.bitwise_not(image)
        
        CHANNEL_DIFFERENCE_TOLORANCE = 1 # 0 ~ 255
        min_rgb = image.min(axis=-1).astype(float)
        max_rgb = image.max(axis=-1).astype(float)
        grayscale_mask = (max_rgb - min_rgb) < CHANNEL_DIFFERENCE_TOLORANCE
        
        TEXT_COLOR_THRESHOLD = 128 # 0 ~ 255
        black_mask = np.all(image < TEXT_COLOR_THRESHOLD, axis=-1)
        
        image = np.full_like(image, 255)
        image[grayscale_mask & black_mask] = [0, 0, 0]
        
        image = cv2.GaussianBlur(image, (3, 3), 0)
        
        cv2.imwrite(output_image_path, image)
        return output_image_path
