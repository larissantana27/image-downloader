from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import os

### Initializing Edge Navegator
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

### List of indian web pages
URL = 'https://www.panashindia.com/newarrivals?cat=3' # OK

driver.get(URL)

### Scrolling Down
height = 0
for i in range (1000):
    height = height + 500
    driver.execute_script(f"window.scroll(0, {height});")
    time.sleep(1)

### Obtaining images URLs 
images_tags = driver.find_elements(By.XPATH, "//img[@id]")
print("Quantity of images: ", len(images_tags))
images_urls = [img.get_attribute('src') for img in images_tags]

### Downloading images
save_directory = r"D:\\.Dataset10022024 - TCC\\indian - housefindya"

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

for i, url in enumerate(images_urls):
    response = requests.get(url, stream=True)
    file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

driver.close()