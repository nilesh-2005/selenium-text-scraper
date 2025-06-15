from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('C:\\Users\\user-name\\Downloads\\chromedriver.exe')

def get_driver():
    # Set options to make browsing easier.
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://punsify.com/goofy-python-jokes/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by='xpath', value='//*[@id="post-59059"]/div/div[2]/ol[1]/li[1]')
    return element.text

print(main())

