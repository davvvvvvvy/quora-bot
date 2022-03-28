from .chrome._version import Chrome
from .utils.login import Login
from .utils.answer import Answer

from selenium.webdriver.common.by import By as by
import time, os, shutil

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, HardwareType

def random_user_agent():
	return UserAgent(software_names=[SoftwareName.CHROME.value], hardware_types={HardwareType.COMPUTER.value}, limit=100).get_random_user_agent()

def init(proxy_address=None, browser_profile=None):
    chrome = Chrome()
    return chrome.webdriver(proxy_address=proxy_address, browser_profile=browser_profile)

def check_login(driver):
    try:
        if driver.find_element(by.XPATH, "//input[@id='email']").is_displayed():
            return False
        return True
    except:
        return True

def start(username, password, proxy=None):
    if not os.path.exists(f'data/browser-profiles/{username.replace("@", "").replace(".", "").replace("com", "")}'):
        driver = init(proxy_address=proxy, browser_profile=username.replace("@", "").replace(".", "").replace("com", ""))
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {"userAgent": f"{random_user_agent()}"})
    else:
        driver = init(proxy_address=proxy, browser_profile=username.replace("@", "").replace(".", "").replace("com", ""))
    driver.get("https://www.quora.com"); time.sleep(7)
    if not check_login(driver):
        print("login")
        Login(driver, username, password)
        time.sleep(7)
    # array = collect_questions(driver, "marvel captain")
    # if array:
    #     for arr in array:
    #         print(arr)
    if Answer(driver, "nice post", "marvel captain"):
        print("good")
    time.sleep(5.5)
    driver.quit()