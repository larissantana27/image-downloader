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
# URL = 'https://japan-avenue.com/collections/japanese-women-kimono' # OK
# URL = 'https://shop.japanobjects.com/collections/womens-yukata' # OK
# URL = 'https://furisode-firstcollection.com/furisode-collection/karankoe/' # OK
# URL = 'https://furisode-firstcollection.com/furisode-collection/tokyo-retro/' # OK
# URL = 'https://furisode-firstcollection.com/furisode-collection/kimono-princess/' # OK
URL = 'https://yuzenkomachi.com/rental/houmongi' # 

# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese - avenue"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. japanobjects"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese - eiyokimono" # apaguei por enquanto
save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. furisode"

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

driver.get(URL)

# Getting the total height of the page
total_height = driver.execute_script("return document.body.scrollHeight")
height = 0
scroll_increment = 500

# Scrolling down to the end of the page
while height < total_height:
    driver.execute_script(f"window.scroll(0, {height});")
    time.sleep(1)

    height += scroll_increment
    new_total_height = driver.execute_script("return document.body.scrollHeight")

    if height >= total_height:
        print("Reached the end of the page.")
        break

    total_height = new_total_height

### Obtaining images URLs 
# images_tags = driver.find_elements(By.XPATH, "//img[@class = 'product-item__primary-image']")
# images_tags = driver.find_elements(By.XPATH, "//img[@class='lazyautosizes lazyloaded']")
# images_tags = driver.find_elements(By.XPATH, "//img[@class='transition--fade-in lazyautosizes lazyloaded']")
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, 'カランコエ')]")
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, '東京レトロ')]")
images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, 'KIMONO PRINCESS')]")
print("Quantity of images: ", len(images_tags))
# images_urls = [img.get_attribute('srcset') for img in images_tags]
images_urls = [img.get_attribute('src') for img in images_tags]
# images_urls_ok = [] 
# for i, url in enumerate(images_urls, start=1):
#     if i > 3:
#         break
#     url_without_size = "https:" + url.split(" ")[0]
#     images_urls_ok.append(url_without_size)
#     print("URL sem o tamanho da imagem:", url_without_size)

### Downloading images
# for i, url in enumerate(images_urls):
# for i, url in enumerate(images_urls_ok, start=57):
# for i, url in enumerate(images_urls, start=618):
# for i, url in enumerate(images_urls, start=638):
for i, url in enumerate(images_urls, start=658):
    print("Link:", url)
    if url:
        response = requests.get(url, stream=True)
        file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)

driver.close()