import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Eco
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_auto_update import check_driver
import pyautogui

check_driver('C:\WINDOWS\system32')
with open('knox.txt', 'r') as f:
    for line in f:
        line = line.strip()
        login, password, domain, timeout = line.split('::')

print('timeout = ', timeout)
timeout = round(int(timeout) / 2)
def mouse():
    pyautogui.moveRel(100, 0, duration=0.01)
    pyautogui.moveRel(0, 100)
    pyautogui.moveRel(-100, 0)
    pyautogui.moveRel(0, -100)
def knox_Update():
    global tr_count
    options = Options()
    # options.add_argument("--headless")  # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox')  # Bypass OS security model
    # options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_experimental_option("prefs", {
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    try:
        driver.get(domain)
        time.sleep(4)
    except:
        print('ошибка - не открылся браузер')
        tr_count += 1
        try:
            driver.stop_client()
            driver.close()
            driver.quit()
        except:
            print('браузер не закрыт')

        return tr_count
    time.sleep(2)

    try:
        driver.find_element(By.XPATH, "/html/body/div[6]/div/button[2]").click()
        driver.find_element(By.ID, "USERID").send_keys(login)
        driver.find_element(By.ID, "USERPASSWORD").send_keys(password)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[4]/button/span").click()
        wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
        print("login_by", login, "\nWith password")
    except:
        try:
            wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
            print("login_by_cookies")
        except:
            tr_count += 1
            print('ошибка при авторизации')
            driver.stop_client()
            driver.close()
            driver.quit()
            return tr_count
    a = 0
    while a < 4:
        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div[8]/div[1]/button").click()
        except:
            print('no notification')
        print('попытка = ', a)
        try:
            c = 0
            while c < 8:
                time.sleep(int(timeout))
                mouse()
                time.sleep(int(timeout))
                driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a").click()
                time.sleep(int(timeout))
                mouse()
                time.sleep(int(timeout))
                driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[3]/a").click()
                c += 1
                print('повтор = ', c)

            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[6]/div[2]/span/img").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[6]/div[3]/dl/dd[2]/button/span").click()
            time.sleep(7)
            mouse()
            # wait.until(Eco.element_to_be_clickable((By.ID, "USERID")))
            # driver.find_element(By.XPATH, "/html/body/div[6]/div/button[2]").click()
            driver.find_element(By.ID, "USERID").send_keys(login)
            driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[2]/input").send_keys(password)
            driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[4]/button/span").click()
            wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
        except:
            a += 1
    try:
        driver.stop_client()
        driver.close()
        driver.quit()
        tr_count += 1
        return tr_count
    except:
        print('браузер не закрыт')
        tr_count += 1
        return tr_count



tr_count = 0

while tr_count < 3:
    print('перезагрузка браузера =', tr_count)
    knox_Update()
else:
    print('ошибка, количество попыток = ', tr_count)



