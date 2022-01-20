from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Eco
from selenium.webdriver.support.wait import WebDriverWait
import sys
import time

with open('C:\\IPA\\knox.txt', 'r') as f:
    for line in f:
        line = line.strip()
        login, password, domain, timeout = line.split('::')

tr_count = 0

options = Options()
options.add_argument("--headless")  # Runs Chrome in headless mode.
options.add_argument('--no-sandbox')  # Bypass OS security model
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument('--disable-extensions')
options.add_experimental_option("prefs", {
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
})
driver = webdriver.Chrome(options=options, executable_path='D:\\chromedriver.exe')


def knox_Update():
    global tr_count
    global timeout
    wait = WebDriverWait(driver, 10)
    driver.delete_all_cookies()
    driver.get(domain)

    try:
        driver.get(domain)
    except:
        driver.stop_client()
        driver.close()
        driver.quit()
        tr_count += 1
    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "/html/body/div[6]/div/button[2]").click()
        driver.find_element(By.ID, "USERID").send_keys(login)
        driver.find_element(By.ID, "USERPASSWORD").send_keys(password)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[4]/button/span").click()
        wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
        print("login_by_password")
    except:
        try:
            wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
            print("login_by_cookies")
        except:
            tr_count += 1
    element = wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
    a = 0
    while a < 4:
        try:
            i = 0
            while i < 10:
                time.sleep(int(timeout))
                driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a").click()
                time.sleep(int(timeout))
                driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[3]/a").click()
                i += 1
                print(i)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[6]/div[2]/span/img").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[6]/div[3]/dl/dd[2]/button/span").click()
            wait.until(
                Eco.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[2]/input")))
            driver.find_element(By.XPATH, "/html/body/div[6]/div/button[2]").click()
            time.sleep(10)
            driver.find_element(By.ID, "USERID").send_keys(login)
            driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[2]/input").send_keys(password)
            driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[4]/button/span").click()
            wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
        except:
            a += 1


knox_Update()

while True:
    if tr_count < 4:
        knox_Update()
    else:
        driver.stop_client()
        driver.close()
        driver.quit()
        sys.exit(1)
