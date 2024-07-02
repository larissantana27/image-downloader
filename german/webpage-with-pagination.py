from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import os

import pyautogui

### Initializing Edge Navegator
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

### List of indian web pages
# URL = 'https://ernstlicht.com/product-category/12-ladies-clothing/97-ladies-dirndls/' # OK
# URL = 'https://www.dirndl.com/en/dirndl/mini-dirndl/' # OK
# URL = 'https://www.dirndl.com/en/dirndl/knee-length-dirndl/' # OK
# URL = 'https://www.dirndl.com/en/dirndl/full-length-dirndl/' # OK
# URL = 'https://www.alpenclassics.co.uk/dirndl/' # OK
### German research
# URL = 'https://www.chiemseer-dirndl.de/kaufen/Damen/Dirndl/' # OK
# URL = 'https://www.trachtenland.de/damen/bekleidung/' # OK
# URL = 'https://www.finest-trachten.de/damen/dirndl/' # OK
URL = 'https://www.krueger-dirndl.de/en/women/clothes/dirndl' # 

driver.get(URL)
# check = pyautogui.locateOnScreen('C:\\Users\\Larissa Santana\\Documents\\UFAL\\TCC\\image-downloader\\german\\humano.png')
# if check is None:
#     print("Captcha NÃO encontrado")
#     check = pyautogui.locateOnScreen('C:\\Users\\Larissa Santana\\Documents\\UFAL\\TCC\\image-downloader\\german\\humano.png') # Tentando encontrar o captcha novamente
# else:
#     print("Captcha encontrado")
#     point_check = pyautogui.center(check)  # Obtendo as coordenadas do captcha
#     pyautogui.click(point_check)  # Clicando no captcha
#     time.sleep(5)  # Aguardando 5 segundos para atualizar a página

# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. ernstlicht"
# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. dirndlmini"
# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. dirndlknee"
# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. dirndlfull"
# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. alpenclassics"
# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. chiemseer-dirndl"
# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. trachtenland"
# save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. finest-trachten"
save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. krueger-dirndl"
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
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='porto-lazyload lazy-load-loaded']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='product--image-normal']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='lazy-cat-done']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='lazyloaded']")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@class, 'lazyloaded')]")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@title, 'Dirndl')]")
    # images_tags = driver.find_elements(By.XPATH, "//picture[@data-picture-class='img-fluid']")
    images_tags = driver.find_elements(By.XPATH, "//img[@class='cs-product-tile__img']")

    new_image_urls = [img.get_attribute('srcset') for img in images_tags]
    # new_image_urls = [img.get_attribute('data-iesrc') for img in images_tags]
    # new_image_urls = [img.get_attribute('src') for img in images_tags]
    print(f"Quantity of images on the page: {len(new_image_urls)}")

    image_urls_refactored = []
    for url in new_image_urls:
        if url.strip():  # Verifica se o URL não está vazio ou apenas contém espaços em branco
            url_without_comma = url.split(" ")[0]
            if url_without_comma.endswith(','):
                url_without_comma = url_without_comma[:-1]
            print("Link:", url_without_comma)
            image_urls_refactored.append(url_without_comma)
        else:
            print("URL vazio encontrado. Ignorando.")

    images_urls.extend(image_urls_refactored)
    return images_urls

def navigate_to_next_page(driver, current_page, URL):
    try:
        next_page = current_page + 1
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@class='next page-numbers']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//i[@class='icon--arrow-right']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//i[@class='icon--arrow-right']")
        # print("Next page icon:", next_page_icon)

        # element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "paging--curent-page-info")))
        # text = element.text
        # last_page = int(text.split(" ")[-1]) 
        # print("Last Page:", last_page)

        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//a[@title='DIRNDL' and @aria-label='DIRNDL']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/dirndl/?p={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/kaufen/Damen/Dirndl/?p={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/damen/bekleidung/?p={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{URL}?page={next_page}']")))
        next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{URL}?p={next_page}']")))
        print("next_page_element:", next_page_element)

        # if next_page_icon and current_page < last_page:
        # if next_page_icon and next_page_element:
        if next_page_element:
            # next_page_url = f"{URL}/page/{next_page}/"
            # next_page_url = f"{URL}?p={next_page}&o=2&n=59"
            # next_page_url = f"{URL}?p={next_page}&o=1&n=24"
            next_page_url = f"{URL}?p={next_page}"
            # next_page_url = f"{URL}?p={next_page}&o=1&n=60"
            # next_page_url = f"{URL}?page={next_page}"
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
# for i, url in enumerate(images_urls):
# for i, url in enumerate(images_urls, start=50):
# for i, url in enumerate(images_urls, start=212):
# for i, url in enumerate(images_urls, start=409):
# for i, url in enumerate(images_urls, start=502):
# for i, url in enumerate(images_urls, start=1008):
# for i, url in enumerate(images_urls, start=1204):
# for i, url in enumerate(images_urls, start=1320):
for i, url in enumerate(images_urls, start=1640):
    print("Link:", url)
    response = requests.get(url, stream=True)
    file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

driver.close()