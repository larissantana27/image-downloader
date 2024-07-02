from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os

### Initializing Edge Navegator
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

### List of indian web pages
# URL = 'https://www.elrocio.fr/24-robes-de-danse' # OK
# URL = 'https://www.flamencoelrocio.com/41-flamenco-dresses-offers' # OK
# URL = 'https://www.vivalaferia.es/en/catalog/category/view/go/42' # OK
# URL = 'https://www.tamaraflamenco.com/en/flamenco-dresses-in-stock-immediate-shipment--74' # OK
# URL = 'https://www.ytutanflamenca.com/50-trajes-de-flamenca' # OK
# Spanish Research
# URL = 'https://www.flamenca.com/categoria-producto/trajes-de-flamenca' # OK
# URL = 'https://mepongoflamenca.com/trajes-de-flamenca/' # OK
# URL = 'https://www.mitrajedeflamenca.es/' # OK
# URL = 'https://flamencaycomplementos.com/en/category-product/flamenco/flamenco-dresses/' # OK
# URL = 'https://www.lolaazahares.com/product-category/nueva-coleccion-minerva-mi-otra-yo/' # OK
URL = 'https://www.sonibel.es/shop/' # OK
driver.get(URL)

# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. elrocio"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. flamencoelrocio"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. vivalaferia"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. tamaraflamenco"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. ytutanflamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. flamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. mepongoflamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. mitrajedeflamenca"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. flamencaycomplementos"
# save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. lolaazahares"
save_directory = r"D:\\.Dataset10022024 - TCC\\spanish\\do. sonibel"
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

scroll_increment = 500

def scroll_to_end(driver):
    height = 0
    total_height = driver.execute_script("return document.body.scrollHeight")

    while height < total_height:
        driver.execute_script(f"window.scroll(0, {height});")
        time.sleep(2)
        height += scroll_increment

    print("Reached the end of the page.")

def process_images(driver, images_urls):
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='img-fluid']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='product-image-photo default_image ']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='replace-2x img-responsive front-image']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='attachment-woocommerce_thumbnail size-woocommerce_thumbnail entered lazyloaded']")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'entered lazyloaded')]")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='attachment-woocommerce_thumbnail size-woocommerce_thumbnail']")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@loading, 'lazy')]")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='attachment-woocommerce_thumbnail size-woocommerce_thumbnail lazyloaded']")
    images_tags = driver.find_elements(By.XPATH, "//img[@class='show-on-hover absolute fill hide-for-small back-image lazy-load-active']")

    new_image_urls = [img.get_attribute('src') for img in images_tags]
    print(f"Quantity of images on the page: {len(new_image_urls)}")

    image_urls_refactored = []
    for url in new_image_urls:
        if url.strip():
            # url_without_comma = url.split(" ")[0]
            # if url_without_comma.endswith(','):
            #     url_without_comma = url_without_comma[:-1]
            # print("Link:", url_without_comma)
            # image_urls_refactored.append(url_without_comma)
            print("Link:", url)
            image_urls_refactored.append(url)
        else:
            print("URL vazio encontrado. Ignorando.")

    images_urls.extend(image_urls_refactored)
    return images_urls

def navigate_to_next_page(driver, current_page, URL):
    try:
        next_page = current_page + 1
        # next_page_icon = driver.find_elements(By.XPATH, f"//i[@class='fa fa-long-arrow-right']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='{URL}/?p={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//i[@class='icon-right-open-3']")
        # print("Next page icon:", next_page_icon)

        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//a[@title='DIRNDL' and @aria-label='DIRNDL']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/en/flamenco-dresses-in-stock-immediate-shipment--74?p={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{URL}?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{URL}/page/{next_page}/']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/?product-page={next_page}']")))
        next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{URL}page/{next_page}/']")))
        print("Next page element:", next_page_element)

        # if next_page_icon and current_page < last_page:
        # if next_page_icon and next_page_element:
        if next_page_element:
            # next_page_url = f"{URL}?p={next_page}"
            # next_page_url = f"{URL}?page={next_page}"
            # next_page_url = f"{URL}/page/{next_page}"
            next_page_url = f"{URL}page/{next_page}/"
            # next_page_url = f"{URL}?product-page={next_page}"
            driver.get(next_page_url)
            print(f"Went to the next page: {next_page_url}")
            time.sleep(2)
            return True
        return False
    
    except Exception as e:
        print("Error navigating to the next page:", e)
        return False

def scrape_pages_recursively(driver, current_page, URL, images_urls):
    scroll_to_end(driver)
    images_urls = process_images(driver, images_urls)
    
    if navigate_to_next_page(driver, current_page, URL):
        images_urls = scrape_pages_recursively(driver, current_page + 1, URL, images_urls)

    return images_urls

initial_page = 1
images_urls = []
images_urls = scrape_pages_recursively(driver, initial_page, URL, images_urls)

### Downloading images
# for i, url in enumerate(images_urls, start=9): #12
# for i, url in enumerate(images_urls, start=502):
# for i, url in enumerate(images_urls, start=698):
# for i, url in enumerate(images_urls, start=770):
# for i, url in enumerate(images_urls, start=1092):
# for i, url in enumerate(images_urls, start=1131):
# for i, url in enumerate(images_urls, start=1272):
# for i, url in enumerate(images_urls, start=1304):
# for i, url in enumerate(images_urls, start=1945):
for i, url in enumerate(images_urls, start=2070):
    print("Link:", url)
    response = requests.get(url, stream=True)
    file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

driver.close()