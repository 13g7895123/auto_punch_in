from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from config.config import *
from line_notify import *
import datetime
import warnings
import time

# 關閉警告
warnings.filterwarnings('ignore', category=DeprecationWarning)

# 關閉瀏覽器通知視窗
options = webdriver.FirefoxOptions()
# options.add_argument('--headless')
options.add_argument('--disable-popup-blocking')

# 爬蟲配置
driver_service = Service(executable_path=driver_path)
driver = webdriver.Firefox(firefox_binary=firefox_path, service=driver_service, options=options)

# 開啟爬蟲
driver.get(web_url)


# 登入
def login():
    # 取得網頁欄位 & 操作網頁
    driver.find_element(By.ID, 'inputEmail').send_keys(email)
    driver.find_element(By.ID, 'inputPassword').send_keys(pwd)
    driver.find_element(By.XPATH, "//button[text()='登入']").click()


# 確認上班
# param: active(0=>打卡前， 1=>打卡後)
def check_punch_in(active):
    tbody = driver.find_element(By.XPATH, "//table[@class='table table-bordered']/tbody")
    punch_count = len(tbody.find_elements(By.XPATH, "tr"))
    now_time = datetime.datetime.now().strftime('%H:%M')
    if active == 0:
        # 判斷時間及打卡狀態
        if '07:55' < now_time < '08:00' and punch_count == 0:
            punch_in_able = 1
        elif '13:25' < now_time < '13:30' and punch_count == 2:
            punch_in_able = 1
        else:
            punch_in_able = 0
        return punch_in_able
    elif active == 1:
        if '07:55' < now_time < '08:00' and punch_count == 1:
            punch_in_finish = 1
        elif '13:25' < now_time < '13:30' and punch_count == 3:
            punch_in_finish = 1
        else:
            punch_in_finish = 0
        return punch_in_finish


# 確認下班
def check_punch_out(active):
    tbody = driver.find_element(By.XPATH, "//table[@class='table table-bordered']/tbody")
    punch_count = len(tbody.find_elements(By.XPATH, "tr"))
    now_time = datetime.datetime.now().strftime('%H:%M')
    if active == 0:
        # 判斷時間及打卡狀態
        if '12:00' < now_time < '12:05' and punch_count == 1:
            punch_out_able = 1
        elif '17:30' < now_time < '17:35' and punch_count == 3:
            punch_out_able = 1
        else:
            punch_out_able = 0
        return punch_out_able
    elif active == 1:
        if '12:00' < now_time < '12:05' and punch_count == 2:
            punch_out_finish = 1
        elif '17:30' < now_time < '17:35' and punch_count == 4:
            punch_out_finish = 1
        else:
            punch_out_finish = 0
        return punch_out_finish


# 打卡上班
def punch_in():
    punch_in_able = check_punch_in(0)   # 確認可以打卡
    if punch_in_able == 1:              # 1為可以打卡
        driver.find_element(By.XPATH, "//button[@class='btn btn-outline-primary']").click()    # 執行打卡
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        alert = driver.switch_to.alert  # 切換至警告視窗
        alert.accept()   # 點擊確定
        time.sleep(3)
        punch_in_finish = check_punch_in(1)     # 確認打卡完成
        print('打卡狀態確認: ' + str(punch_in_finish))
        if punch_in_finish == 1:                # 1為打卡完成
            line_notify('\n上班打卡作業完成')
        else:
            line_notify('\n上班打卡作業未完成，請重新確認')
    else:
        line_notify('\n上班打卡作業未完成，請重新確認')
    driver.quit()


# 打卡下班
def punch_out():
    punch_out_able = check_punch_out(0)  # 確認可以打卡
    if punch_out_able == 1:              # 1為可以打卡
        driver.find_element(By.XPATH, "//button[@class='btn btn-outline-danger ']").click()  # 執行打卡
        driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
        alert = driver.switch_to.alert  # 切換至警告視窗
        alert.accept()  # 點擊確定
        time.sleep(3)
        punch_out_finish = check_punch_out(1)  # 確認打卡完成
        print('打卡狀態確認: ' + str(punch_out_finish))
        if punch_out_finish == 1:              # 1為打卡完成
            line_notify('\n下班打卡作業完成')
        else:
            line_notify('\n下班打卡作業未完成，請重新確認')
    else:
        line_notify('\n下班打卡作業未完成，請重新確認')
    driver.quit()


# 測試用
# login()
# driver.find_element(By.XPATH, "//button[@class='btn btn-outline-danger ']").click()  # 執行打卡
# input('test')
# driver.quit()
