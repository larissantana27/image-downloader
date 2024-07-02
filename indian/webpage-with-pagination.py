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
# URL = 'https://www.fabricoz.com/collections/indian-dresses-online-all' # OK
URL = 'https://www.kalkifashion.com/ethnic/organza-sarees.html' # OK
driver.get(URL)

# save_directory = r"D:\\.Dataset10022024 - TCC\\indian\\do. fabricoz"
save_directory = r"D:\\.Dataset10022024 - TCC\\indian\\do. kalkifashion"
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
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@src, 'https://www.fabricoz.com/cdn/shop/products/')]")
    images_tags = driver.find_elements(By.XPATH, "//div[contains(@id, 'hover')]")

    new_image_urls = [img.get_attribute('src') for img in images_tags]
    # new_image_urls = [img.get_attribute('hoversrc') for img in images_tags]
    # new_image_urls = [img.get_attribute('data-original') for img in images_tags]
    print(f"Quantity of images on the page: {len(new_image_urls)}")

    image_urls_refactored = []
    for url in new_image_urls:
        print("Link:", url)
        image_urls_refactored.append(url)

    images_urls.extend(image_urls_refactored)
    return images_urls

def navigate_to_next_page(driver, current_page, URL):
    try:
        next_page = current_page + 1
        # next_page_icon = driver.find_element(By.XPATH, "//span[@aria-label='Next']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//span[@aria-description='Next']")
        # print("Next page icon:", next_page_icon)

        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/indian-dresses-online-all?page={next_page}']")))
        next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{URL}?p={next_page}']")))
        
        print("Next page element:", next_page_element)

        # if next_page_element:
        # if next_page_icon and next_page_element:
        if next_page_element and next_page < 5:
            next_page_url = f"{URL}?page={next_page}"
            # next_page_url = f"{URL}?p={next_page}"
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
# for i, url in enumerate(images_urls, start=502):
# for i, url in enumerate(images_urls, start=770):
# for i, url in enumerate(images_urls, start=1065):
# for i, url in enumerate(images_urls, start=1624):
for i, url in enumerate(images_urls, start=1780):
    print("Link:", url)
    response = requests.get(url, stream=True)
    file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

driver.close()