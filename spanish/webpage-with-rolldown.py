from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import os

### Initializing Edge Navegator
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

### List of german web pages
# URL = 'https://www.lunaresflamenco.com.br/en/16-flamenco-dresses' # OK
# URL = 'https://www.vestidosdesevillanas.com/mujer/trajes-colecciones-seora/index.php' # OK
### Spanish Research
# URL = 'https://micaelavilla.com/flamenca/' # OK
# URL = 'https://sibilinaflamenca.es/categoria-producto/shop/flamenca/' # OK
# URL = 'https://laboutiqueflamenca.com/trajes-de-flamenca/' # OK
# URL = 'https://saradebenitez.com/moda-exclusiva/moda-flamenca/trajes-flamenca/' # OK
# URL = 'https://yolandamodaflamenca.com/trajes-de-flamenca-mujer/' # OK
# URL = 'https://carolymodaflamenca.es/categoria-producto/vestidos-flamenca/' # OK
# URL = 'https://www.isabelhernandez.es/categoria-producto/colecciones/trajes-de-flamenca/' # OK
URL = 'https://trajesdeflamencalolaylo.com/category/vestidos/' # OK 

driver.get(URL)

# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. lunaresflamenco"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. vestidosdesevillanas"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. micaelavilla"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. sibilinaflamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. laboutiqueflamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. saradebenitez"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. yolandamodaflamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. carolymodaflamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. isabelhernandez"
save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. trajesdeflamencalolaylo"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Getting the total height of the page
total_height = driver.execute_script("return document.body.scrollHeight")
height = 0
scroll_increment = 500

# Scrolling down to the end of the page
while height < total_height:
    driver.execute_script(f"window.scroll(0, {height});")
    time.sleep(2)

    height += scroll_increment
    new_total_height = driver.execute_script("return document.body.scrollHeight")

    if height >= total_height:
        print("Reached the end of the page.")
        break

    total_height = new_total_height

### Obtaining images URLs 
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'replace-2x img-responsive')]")
# images_tags = driver.find_elements(By.XPATH, "//img[@class='img-responsive img-equalized']")
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'attachment-medium_large size-medium_large wp-image')]")
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'attachment-woocommerce_thumbnail size-woocommerce_thumbnail')]")
# images_tags = driver.find_elements(By.XPATH, "//a[contains(@class, 'e-gallery-item elementor-gallery-item')]")
# images_tags = driver.find_elements(By.XPATH, "//a[@class='e-gallery-item elementor-gallery-item elementor-animated-content']")
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'attachment-woocommerce_thumbnail')]")
# images_tags = driver.find_elements(By.XPATH, "//img[@class='woo-entry-image-main']")
# images_tags = driver.find_elements(By.XPATH, "//img[@class='attachment-shop_catalog size-shop_catalog wp-post-image']")
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'lazyloaded')]")
# images_tags = driver.find_elements(By.XPATH, "//img[@class='attachment-woocommerce_thumbnail size-woocommerce_thumbnail wp-post-image']")
images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'aligncenter')]")
print("Quantity of images: ", len(images_tags))
images_urls = [img.get_attribute('src') for img in images_tags]
# images_urls = [img.get_attribute('href') for img in images_tags]
# images_urls = [img.get_attribute('data-thumbnail') for img in images_tags]

images_urls_ok = [] 
for i, url in enumerate(images_urls, start=1):
    # if i > 3:
    #     break
    # url_without_size = "https:" + url.split(" ")[0]
    # url_without_size = {URL} + url.split("/")[2]
    # url_without_size = url.split(", ")[0]
    # url_without_size = url.split(" ")[0]
    # url_without_size = {URL} + url
    url_without_size = url
    images_urls_ok.append(url_without_size)
    print("URL sem o tamanho da imagem:", url_without_size)

### Downloading images
# for i, url in enumerate(images_urls):
# for i, url in enumerate(images_urls, start=917):
# for i, url in enumerate(images_urls_ok, start=1056):
# for i, url in enumerate(images_urls, start=1068):
# for i, url in enumerate(images_urls, start=1092):
# for i, url in enumerate(images_urls, start=1327):
# for i, url in enumerate(images_urls, start=1412):
# for i, url in enumerate(images_urls, start=1694):
# for i, url in enumerate(images_urls, start=1737):
for i, url in enumerate(images_urls, start=2006):
    # print("Link: ", url)
    if url:
        response = requests.get(url, stream=True)
        file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)

driver.close()