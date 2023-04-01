from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_experimental_option('detach', True)

website = "https://www.amazon.com/s?k=gaming+headsets&pd_rd_r=9254108a-3059-4d5e-a17e-ebd102c33001&pd_rd_w=2JvCb&pd_rd_wg=5uIqU&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=2M1S59K324M7A8TDDB7Z&ref=pd_gw_unk"

browser = webdriver.Chrome(options=options)
browser.get(website)


isNextDisabled = False

while not isNextDisabled:
    button_element = WebDriverWait(browser, 50).until(
        EC.presence_of_element_located((By.CLASS_NAME, "s-pagination-next")))
    try:
        products_main_div = browser.find_element(
            By.XPATH, '//*[@id="search"]/div[1]/div[1]')
        products = products_main_div.find_elements(
            By.XPATH, '//div[@data-component-type="s-search-result"]')

        print(len(products))

        # for product in products:
        #     product_name = product.find_element(By.TAG_NAME, 'h2').text
        #     price = "No Price Found"
        #     img = "No image Found"
        #     url = "No Url Found"
        #     try:
        #         price = product.find_element(
        #             By.XPATH, '//span[@class="a-price"]').text.replace("\n", ".")
        #     except:
        #         pass

        #     try:
        #     img = product.find_element(By.TAG_NAME, "img").get_attribute("src")
        # except:
        #     pass

        # try:
        #     url= product.find_element(By.XPATH,'//a[@class="a-link-normal"]').get_attribute("href")
        # except:
        #     pass
        # print("Name = " +product_name)
        # print("Price = " +price.strip("$"))
        # print("Image ="+img)
        # print("Url ="+url + "\n")

        try:
            next_button = browser.find_element(
                By.CLASS_NAME, "s-pagination-next")
            next_button = WebDriverWait(browser, 50).until(
                EC.presence_of_element_located((By.CLASS_NAME, "s-pagination-next")))
            next_button.click()
            print("button clicked")
        except Exception as e:
            print(e, "Pagination Error")
            isNextDisabled = True

    except Exception as e:
        print(e, "Main Error")

