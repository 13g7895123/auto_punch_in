from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from config.config import *
from line_notify import *

# 爬蟲配置
driver_service = Service(executable_path=driver_path)
driver = webdriver.Firefox(firefox_binary=firefox_path, service=driver_service)

# 開啟爬蟲
driver.get(web_url)


# 登入
def login():
    # 取得網頁欄位
    input_email = driver.find_element(By.ID, 'inputEmail')
    input_pwd = driver.find_element(By.ID, 'inputPassword')
    login_btn = driver.find_element(By.XPATH, "//button[text()='登入']")

    # 操作網頁
    input_email.send_keys(email)
    input_pwd.send_keys(pwd)
    login_btn.click()


# 打卡上班
def punch_in():
    punch_in_btn = driver.find_element(By.XPATH, "//button[text()='打卡上班']")
    punch_in_btn.click()


# 打卡下班
def punch_out():
    punch_out_btn = driver.find_element(By.XPATH, "//button[text()='打卡下班']")
    punch_out_btn.click()

# 確認上班
# def check_punch_in():

# 確認下班
# def check_punch_out():
