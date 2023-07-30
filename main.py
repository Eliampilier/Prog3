import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest import mark

def save_image(driver, path):
    hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    driver.save_screenshot(f"./screenshots/{path}/screen{hora}.png")
    return

@mark.parametrize("name,password", [("carlo", "pass"), ("francis", "12345"), ("chavito", "55"), ("admin", "123456")])
def testPage(name, password):
    driver = webdriver.Chrome()
    driver.get("https://projects.devlup.com/LoginSystemv45/admin_login.php")
    driver.find_element(By.ID, 'inputEmail').send_keys(name)
    driver.find_element(By.ID, 'inputPassword').send_keys(password)
    driver.find_element(By.XPATH, '//button').click()
    save_image(driver, 'login')
    assert driver.current_url != "https://projects.devlup.com/LoginSystemv45/admin_login.php"

def testLogoutSideBar():
    driver = webdriver.Chrome()
    driver.get("https://projects.devlup.com/LoginSystemv45/admin_login.php")
    driver.find_element(By.ID, 'inputEmail').send_keys('admin')
    driver.find_element(By.ID, 'inputPassword').send_keys('123456')
    driver.find_element(By.XPATH, '//button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//li[7]').click()
    time.sleep(3)
    save_image(driver, 'logout')
    assert driver.current_url == "https://projects.devlup.com/LoginSystemv45/admin_login.php"

def testLogoutMenu():
    driver = webdriver.Chrome()
    driver.get("https://projects.devlup.com/LoginSystemv45/admin_login.php")
    driver.find_element(By.ID, 'inputEmail').send_keys('admin')
    driver.find_element(By.ID, 'inputPassword').send_keys('123456')
    driver.find_element(By.XPATH, '//button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//div[@id="wrapper"]/nav/ul/li/a').click()
    driver.find_element(By.XPATH, '//*[@id="wrapper"]/nav/ul/li/ul/li/a').click()
    time.sleep(3)
    save_image(driver, 'logoutmenu')
    assert driver.current_url == "https://projects.devlup.com/LoginSystemv45/admin_login.php"

def testUserList():
    driver = webdriver.Chrome()
    driver.get("https://projects.devlup.com/LoginSystemv45/admin_login.php")
    driver.find_element(By.ID, 'inputEmail').send_keys('admin')
    driver.find_element(By.ID, 'inputPassword').send_keys('123456')
    driver.find_element(By.XPATH, '//button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//ul[@id="side-menu"]/li[3]/a').click()
    save_image(driver, 'userlist')
    assert driver.current_url == "https://projects.devlup.com/LoginSystemv45/admin_user_list.php"

def testUserList():
    driver = webdriver.Chrome()
    driver.get("https://projects.devlup.com/LoginSystemv45/admin_login.php")
    driver.find_element(By.ID, 'inputEmail').send_keys('admin')
    driver.find_element(By.ID, 'inputPassword').send_keys('123456')
    driver.find_element(By.XPATH, '//button').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//ul[@id="side-menu"]/li[5]/a').click()
    save_image(driver, 'roles')
    assert driver.current_url == "https://projects.devlup.com/LoginSystemv45/admin_user_role.php"

