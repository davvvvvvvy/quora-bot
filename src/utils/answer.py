# https://www.quora.com/search?q=marvel
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as k
import time, random

BLACK_LIST = ["/profile", "/following", "/answer", "/spaces", "/notifications", "/topic/", "/profile", "/unanswered", "/messages/new", "/messages/"]

def scroll(driver):
    try:
        i=0
        rand = random.randint(1, 5)
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(1.5)
            i+=1
            if i == rand:
                break
    except:
        pass

def collect_questions(driver, tags):
    tags = tags.replace(" ", "+")
    driver.get(f"https://www.quora.com/search?q={tags}"); time.sleep(7)
    try:
        scroll(driver)
        maincontent = driver.find_element(by.XPATH, "//div[@class='q-box']")
        links = maincontent.find_elements(by.TAG_NAME, "a")
        array=[]
        for link in links:
            try:
                if "https://www.quora.com/" == link.get_attribute("href"):
                    continue
                logic=False
                for black_list in BLACK_LIST:
                    if black_list in link.get_attribute("href"):
                        logic=True
                if logic:
                    continue
                array.append(link.get_attribute("href"))
            except:
                pass
        return array
    except:
        pass
    return None

def Answer(driver, message, tags):
    array = collect_questions(driver, tags)
    if not array:
        return False
    for arr in array:
        driver.get(arr); time.sleep(7)
        try:
            for button in driver.find_elements(by.TAG_NAME, "button"):
                for div in button.find_elements(by.TAG_NAME, "div"):
                    if "Answer" in div.text:
                        button.click(); time.sleep(1.5)
                        break
        except:
            pass
        try:
            textarea = driver.find_element(by.XPATH, "//div[@class='doc empty']")
            textarea.click(); textarea.send_keys(message); time.sleep(1.5)
            try:
                for button in driver.find_elements(by.TAG_NAME, "button"):
                    for div in button.find_elements(by.TAG_NAME, "div"):
                        if "Post" in div.text:
                            button.click(); time.sleep(1.5)
            except:
                pass
        except:
            pass