from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from config.config import *

# 瀏覽器路徑
firefox_path = firefox_path

# 爬蟲配置
driver_service = Service(executable_path=driver_path)
driver = webdriver.Firefox(firefox_binary=firefox_path, service=driver_service)
driver.get(web_url)

# 取得網頁欄位
input_email = driver.find_element(By.ID, 'inputEmail')
input_pwd = driver.find_element(By.ID, 'inputPassword')
login_btn = driver.find_element(By.CLASS_NAME, 'btn')
punch_in_btn = driver.find_element(By.XPATH, "//button[text()='打卡上班']")
punch_out_btn = driver.find_element(By.XPATH, "//button[text()='打卡下班']")

# 操作網頁
input_email.send_keys(email)
input_pwd.send_keys(pwd)
login_btn.click()



# driver.close()


