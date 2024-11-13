from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import os

class CardDownloader():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("headless")
        self.driver = webdriver.Chrome(options=self.options)
    

    def download_image(self, card_name, image_dir):
        self.driver.get("https://pkmncards.com/?s=" + card_name)
        print("Found " + card_name)
        img_elem = self.driver.find_element(By.CLASS_NAME, "card-image")
        src = img_elem.get_attribute('src')
        urllib.request.urlretrieve(src, os.path.join(image_dir, card_name + ".jpg"))


