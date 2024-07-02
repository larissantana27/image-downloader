from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
import requests
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

### Initializing Edge Navegator
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

### List of indian web pages
# URL = 'https://japan-clothing.com/collections/japanese-women-kimono' # OK
# URL = 'https://kimurakami.com/collections/japanese-kimono-dress' # OK
### Japanese research
# URL = 'https://kimono-hearts-store.com/collections/neojapanesque' # OK
# URL = 'https://kimono-hearts-store.com/collections/gothic' # OK
# URL = 'https://kimono-hearts-store.com/collections/mode-style' # OK
# URL = 'https://kimono-hearts-store.com/collections/ikikoten' # OK
# URL = 'https://kimono-hearts-store.com/collections/street-co'# OK
# URL = 'https://kimono-hearts-store.com/collections/dentoukoten' # OK
# URL = 'https://kimono-hearts-store.com/collections/maihimekoten' # OK
# URL = 'https://kimono-hearts-store.com/collections/taisyouromanesuku' # OK
# URL = 'https://kimono-hearts-store.com/collections/frontpage' # OK
# URL = 'https://toiki.jp/fs/toiki/c/toiki218' # OK
# URL = 'https://toiki.jp/fs/toiki/c/gr509' # OK
# URL = 'https://toiki.jp/fs/toiki/GoodsSearchList.html?_e_k=%82%60&keyword=1A000454' # OK
# URL = 'https://global.kimono-yamato.com/Form/Product/ProductList.aspx?shop=0&cat=199001' # OK
# URL = 'https://global.kimono-yamato.com/Form/Product/ProductList.aspx?shop=0&cat=199002' #OK
# URL = 'https://global.kimono-yamato.com/Form/Product/ProductList.aspx?shop=0&cat=199002&pgi=
    # &cicon=&dosp=&dpcnt=-1&img=2&max=&min=&sort=07&swrd=&udns=2&fpfl=0&col=&bids=&cols=&pno=2' # OK
# URL = 'https://global.kimono-yamato.com/Form/Product/ProductList.aspx?shop=0&cat=199003'
# URL = 'https://komaya.info/gallery/?s_cate=12&s_type=#links' # OK
# URL = 'https://komaya.info/gallery/?s_cate=11&s_type=#links' # OK
# URL = 'https://www.the-kimonoshop.jp/collections/all' # OK
# URL = 'https://www.kimonomachi.co.jp/c/kimono/araerukimono' # OK
# URL = 'https://www.kimonomachi.co.jp/p/search?keyword=%E6%9C%A8%E7%B6%BF&sort=priority' # OK
# URL = 'https://www.furisodeshop.com/collection/' # OK
# URL = 'https://www.furisodeshop.com/collection/page/2/' # OK

# URL = 'https://mgos.jp/shop/mimatsu/c/c100102/' # OK
# URL = 'https://mgos.jp/shop/mimatsu/c/c100105/' # OK
# URL = 'https://mgos.jp/shop/mgos/r/rgr18/' # OK
URL = 'https://mgos.jp/shop/mgos/r/rgr20/' # OK

driver.get(URL)

# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. japan-clothing"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. kimurakami"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. kimono-hearts-store"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. toiki"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. global.kimono-yamato2"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. komaya"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. the-kimonoshop.jp"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. kimonomachi"
# save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. furisodeshop"
save_directory = r"D:\\.Dataset10022024 - TCC\\japanese\\do. mgos"
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
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='grid-product__image lazyautosizes lazyloaded']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='ProductItem__Image Image--fadeIn lazyautosizes Image--lazyLoaded']")
    # images_tags = driver.find_elements(By.XPATH, "//img[@class='lazyload-fade lazyautosizes lazyloaded']")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@src, '/shop/item/toiki/picture/goods')]")  
    # images_tags = driver.find_elements(By.XPATH, "//img[@id='imgProductImage']")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, '振袖')]")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, '卒業袴')]")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, 'カランコエ')]")
    images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, '|')]")
    # images_tags = driver.find_elements(By.XPATH, "//img[contains(@alt, '【プレタ小紋】')]")

    # new_image_urls = [img.get_attribute('srcset') for img in images_tags]
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
            # image_urls_refactored.append(url_without_comma)
            # print("Link:", "https:"+url)
            # image_urls_refactored.append("https://mgos.jp"+url)
            print("Link:", url)
            image_urls_refactored.append(url)
        else:
            print("URL vazio encontrado. Ignorando.")

    images_urls.extend(image_urls_refactored)
    return images_urls

def navigate_to_next_page(driver, current_page, URL):
    try:
        next_page = current_page + 1
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/japanese-women-kimono?p={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/japanese-kimono-dress?page={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/gothic?page={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/mode-style?page={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/ikikoten?page={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/street-co?page={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/dentoukoten?page={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/maihimekoten?page={next_page}']")
        # next_page_icon = driver.find_elements(By.XPATH, f"//a[@href='/collections/taisyouromanesuku?page={next_page}']")
        # next_page_icon = driver.find_elements((By.XPATH, "//a[contains(@href, 'pno={next_page}')]"))
        # print("Next page icon:", next_page_icon)

        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/japanese-kimono-dress?p={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/japanese-kimono-dress?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/gothic?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/mode-style?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/ikikoten?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/street-co?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/dentoukoten?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/maihimekoten?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/taisyouromanesuku?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/frontpage?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href, '{URL}/1/{next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/Form/Product/ProductList.aspx?shop=0&cat=199001&pgi=&cicon=&dosp=&dpcnt=-1&img=2&max=&min=&sort=07&swrd=&udns=2&fpfl=0&col=&bids=&cols=&pno={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/Form/Product/ProductList.aspx?shop=0&cat=199003&pgi=&cicon=&dosp=&dpcnt=-1&img=2&max=&min=&sort=07&swrd=&udns=2&fpfl=0&col=&bids=&cols=&pno={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='https://komaya.info/gallery/page/{next_page}/?s_cate=12&s_type']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='https://komaya.info/gallery/page/{next_page}/?s_cate=11&s_type']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/collections/all?page={next_page}']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/c/kimono/araerukimono?page={next_page}&sort=priority']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/p/search?keyword=%E6%9C%A8%E7%B6%BF&page={next_page}&sort=priority']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='https://www.furisodeshop.com/collection/page/2{next_page}/']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/shop/mimatsu/c/c100102_p{next_page}/']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/shop/mimatsu/c/c100105_p{next_page}/']")))
        # next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/shop/mgos/r/rgr18_p{next_page}/']")))
        next_page_element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, f"//a[@href='/shop/mgos/r/rgr20_p{next_page}/']")))
        print("Next page element:", next_page_element)

        # if next_page_icon and current_page < last_page:
        # if next_page_icon and next_page_element:
        if next_page_element:
            # next_page_url = f"{URL}?p={next_page}"
            # next_page_url = f"{URL}?page={next_page}"
            # next_page_url = f"{URL}/1/{next_page}"
            # next_page_url = f"{URL}&pgi=&cicon=&dosp=&dpcnt=-1&img=2&max=&min=&sort=07&swrd=&udns=2&fpfl=0&col=&bids=&cols=&pno={next_page}"
            # next_page_url = f"https://komaya.info/gallery/page/{next_page}/?s_cate=12&s_type"
            # next_page_url = f"https://komaya.info/gallery/page/{next_page}/?s_cate=11&s_type"
            # next_page_url = f"{URL}?page={next_page}&sort=priority"
            # next_page_url = f"https://www.kimonomachi.co.jp/p/search?keyword=%E6%9C%A8%E7%B6%BF&page={next_page}&sort=priority"
            # next_page_url = f"{URL}/page/{next_page}/"
            # next_page_url = f"https://mgos.jp/shop/mimatsu/c/c100102_p{next_page}/"
            # next_page_url = f"https://mgos.jp/shop/mimatsu/c/c100105_p{next_page}/"
            # next_page_url = f"https://mgos.jp/shop/mgos/r/rgr18_p{next_page}/"
            next_page_url = f"https://mgos.jp/shop/mgos/r/rgr20_p{next_page}/"
            driver.get(next_page_url)
            print(f"Went to the next page: {next_page_url}")
            time.sleep(4)
            return True
        return False
    
    except Exception as e:
        print("Error navigating to the next page:", e)
        return False

def scrape_pages_recursively(driver, current_page_number, URL, images_urls):
    scroll_to_end(driver)
    images_urls = process_images(driver, images_urls)
    
    if navigate_to_next_page(driver, current_page_number, URL):
        images_urls = scrape_pages_recursively(driver, current_page_number + 1, URL, images_urls)

    return images_urls

initial_page_number = 1
images_urls = []
images_urls = scrape_pages_recursively(driver, initial_page_number, URL, images_urls)

### Downloading images
# for i, url in enumerate(images_urls, start=60):
# for i, url in enumerate(images_urls, start=99):
# for i, url in enumerate(images_urls, start=174):
# for i, url in enumerate(images_urls, start=197):
# for i, url in enumerate(images_urls, start=232):
# for i, url in enumerate(images_urls, start=254):
# for i, url in enumerate(images_urls, start=284):
# for i, url in enumerate(images_urls, start=296):
# for i, url in enumerate(images_urls, start=383):
# for i, url in enumerate(images_urls, start=417):
# for i, url in enumerate(images_urls, start=446):
# for i, url in enumerate(images_urls, start=477):
# for i, url in enumerate(images_urls, start=481):
# for i, url in enumerate(images_urls, start=505):
# for i, url in enumerate(images_urls, start=511):
# for i, url in enumerate(images_urls, start=570):
# for i, url in enumerate(images_urls, start=611):
# for i, url in enumerate(images_urls, start=678):
# for i, url in enumerate(images_urls, start=822):
# for i, url in enumerate(images_urls, start=1818):
# for i, url in enumerate(images_urls, start=2065):
# for i, url in enumerate(images_urls, start=2165):
# for i, url in enumerate(images_urls, start=2231):
# for i, url in enumerate(images_urls, start=2432):
# for i, url in enumerate(images_urls, start=2487):
# for i, url in enumerate(images_urls, start=2604):
# for i, url in enumerate(images_urls, start=2763):
for i, url in enumerate(images_urls, start=3231):
    print("Link:", url)
    response = requests.get(url, stream=True)
    file_path = os.path.join(save_directory, f'img-{i+1}.jpg')
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

driver.close()

# 2166-2442 - komaya
# 2443-2846 - global.kimono-yamato2