from .captcha_solve import solve

from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as k
import time, random

def Login(driver, email, password):
    # driver.get("https://www.quora.com"); time.sleep(7)
    try:
        if driver.find_element(by.XPATH, "//input[@id='email']").is_displayed() and driver.find_element(by.XPATH, "//input[@id='password']").is_displayed():
            pass
        else:
            return
    except:
        pass
    try:
        username = driver.find_element(by.XPATH, "//input[@id='email']")
        passwrd = driver.find_element(by.XPATH, "//input[@id='password']")

        username.click(); username.send_keys(email); time.sleep(0.5)
        passwrd.click(); passwrd.send_keys(password); time.sleep(0.5)
        passwrd.send_keys(k.ENTER); time.sleep(0.5)
        driver.find_element(by.TAG_NAME, "body").click(); time.sleep(2.5)
    except:
        pass

    try:
        driver.find_element(by.XPATH, "//iframe[@title='reCAPTCHA']").click(); time.sleep(5.5)
        solve(driver)
    except:
        return

    driver.switch_to.default_content()
    time.sleep(5.5)

    try:
        driver.find_element(by.XPATH, "//button[contains(text(), 'Login')]").click(); time.sleep(5.5)
    except:
        try:
            driver.find_element(by.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[2]/div[2]/div[5]/button").click(); time.sleep(5.5)
        except:
            try:
                driver.find_elements(by.XPATH, "//div[contains(text(), 'Login')]")[1].click(); time.sleep(5.5)
            except:
                try:
                    passwrd.send_keys(k.ENTER); time.sleep(5.5)
                except:
                    pass