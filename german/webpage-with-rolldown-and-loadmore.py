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
# URL = 'https://trachtenhimmel.de/dirndl-mini/?p=1' # OK
# URL = 'https://trachtenhimmel.de/dirndl-midi/?p=1' # OK
URL = 'https://trachtenhimmel.de/dirndl-lang/?p=1' # OK

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

    # Getting the new total height after scrolling
    new_total_height = driver.execute_script("return document.body.scrollHeight")

    if height >= total_height:
        print("Reached the end of the page.")
        break

    # Updating the total height for the next iteration
    total_height = new_total_height

    # Clicking the "load more" button until there's no more
    while True:
        try:
            load_more_button = driver.find_element(By.XPATH, "//a[@class='btn is--primary is--icon-right js--load-more']")
            if load_more_button.is_displayed():
                load_more_button.click()
                time.sleep(2)  # Wait for additional content to load (increase if necessary)
            else:
                break  # If the button is no longer visible, exit the loop

        except Exception as e:
            print("Error clicking 'LOAD MORE' button:", e)
            break  # In case of error, exit the loop to avoid an infinite loop

### Obtaining images URLs 
# images_tags = driver.find_elements(By.XPATH, "//img[contains(@src, '/d3.jpg')]")
images_tags = driver.find_elements(By.XPATH, "//img[contains(@title, 'Dirndl')]")

print("Number of images after loading all:", len(images_tags))
# images_urls = [img.get_attribute('src') for img in images_tags]
images_urls = [img.get_attribute('srcset') for img in images_tags]

image_urls_refactored = []
for url in images_urls:
    if url.strip():  # Verifica se o URL não está vazio ou apenas contém espaços em branco
        url_without_comma = url.split(" ")[0]
        if url_without_comma.endswith(','):
            url_without_comma = url_without_comma[:-1]
        print("Link:", url_without_comma)
        image_urls_refactored.append(url_without_comma)
    else:
        print("URL vazio encontrado. Ignorando.")

images_urls.extend(image_urls_refactored)

### Downloading images
save_directory = r"D:\\.Dataset10022024 - TCC\\german\\do. trachtenhimmel"

if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# for i, url in enumerate(images_urls, start=1640):
# for i, url in enumerate(images_urls, start=2054):
for i, url in enumerate(images_urls, start=3024):
    response = requests.get(url, stream=True)
    file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

driver.close()