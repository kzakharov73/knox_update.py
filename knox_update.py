import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Eco
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui
import pyfiglet
from colorama import init, Fore, Back, Style
from webdriver_auto_update.chrome_app_utils import ChromeAppUtils
from webdriver_auto_update.webdriver_manager import WebDriverManager
import win32api
import win32con


privet = pyfiglet.figlet_format('KNOX ROBOT')
print(Style.BRIGHT + Fore.GREEN)
print(privet)
# Using ChromeAppUtils to inspect Chrome application version
chrome_app_utils = ChromeAppUtils()


# Target directory to store chromedriver
driver_directory = "C:\WINDOWS\system32"

# Create an instance of WebDriverManager
driver_manager = WebDriverManager(driver_directory)

# Call the main method to manage chromedriver
driver_manager.main()

dir_path = os.getcwd()
user_profile_path = os.environ['USERPROFILE']
user_profile_path.replace('/', '\\\\')

with open('knox.txt', 'r') as f:
    for line in f:
        line = line.strip()
        login, password, domain, timeout = line.split('::')

print(Fore.RED, 'timeout = ', timeout)
timeout = round(int(timeout)/2)


def mouse():
    pyautogui.moveRel(100, 0, duration=0.01)
    pyautogui.moveRel(0, 100)
    pyautogui.moveRel(-100, 0)
    pyautogui.moveRel(0, -100)


def knox_Update():
    global tr_count

    options = Options()
    options.add_argument("--user-data-dir=" + user_profile_path + '\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 20)
    try:
        driver.get(domain)
        time.sleep(4)
    except:
        print('chrome not open')
        tr_count += 1
        try:
            driver.stop_client()
            driver.close()
            driver.quit()
        except:
            print('chrome not close')

        return tr_count
    time.sleep(2)

    try:
        # driver.find_element(By.XPATH, "/html/body/div[6]/div/button[2]").click()
        driver.find_element(By.ID, "USERID").clear()
        driver.find_element(By.ID, "USERID").send_keys(login)
        driver.find_element(By.ID, "USERPASSWORD").click()
        driver.find_element(By.ID, "USERPASSWORD").send_keys(password)
        time.sleep(10)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/form/div/fieldset/ul/li[4]/button/span").click()
        wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
        print("login_by", login, "\nWith password")
    except:
        try:
            wait.until(Eco.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a")))
            print("login_by_cookies")
        except:
            tr_count += 1
            print('authorization error ')
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
        print(Fore.BLUE, 'try_count = ', a)
        try:
            c = 0
            while c < 10:
                time.sleep(int(timeout))
                win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # press
                win32api.Sleep(5)
                win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)  # release
                mouse()
                time.sleep(int(timeout))
                driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[4]/a").click()
                time.sleep(int(timeout))
                win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # press
                win32api.Sleep(5)
                win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)  # release
                mouse()
                time.sleep(int(timeout))
                driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/ul/li[3]/a").click()
                c += 1
                print('retry = ', c)

            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[6]/div[2]/span/img").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[6]/div[3]/dl/dd[2]/button/span").click()
            time.sleep(7)
            mouse()
            win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # press
            win32api.Sleep(5)
            win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)  # release
            wait.until(Eco.element_to_be_clickable((By.ID, "USERID")))
            driver.find_element(By.ID, "USERID").click()
            driver.find_element(By.ID, "USERID").clear()
            driver.find_element(By.ID, "USERID").send_keys(login)
            driver.find_element(By.ID, "USERPASSWORD").send_keys(password)
            win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # press
            win32api.Sleep(5)
            win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)  # release
            time.sleep(10)
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
        print('chrome do not close')
        tr_count += 1
        return tr_count


tr_count = 0

while tr_count < 6:
    print(Fore.MAGENTA, 'chrome reboot =', tr_count)
    win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)  # press
    win32api.Sleep(5)
    win32api.keybd_event(win32con.VK_UP, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)  # release
    knox_Update()
else:
    print(Fore.RED, 'error, try counter = ', tr_count)
