# 檔案路徑
firefox_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver_path = r'D:\Python\Tools\geckodriver.exe'

# 網址
web_url = 'https://clock.eng-astra.com.tw/clock-system.php'

# 輸入資料
email = 'astra235@3tsai.com'
pwd = 'Astrawm867'

# Line Token
token = 'W4Trvnii3ORUZpusao0lqIAsLVWFXqhoxTyyOwjVBb5'

# punch_time
punch_in_morning = '7:55, 8:00'
punch_in_noon = '13:55, 13:30'
punch_out_noon = '12:00, 12:05'
punch_out_afternoon = '13:55, 13:30'

punch_in_morning_start = punch_in_morning.split(', ')[0]
punch_in_morning_end = punch_in_morning.split(', ')[1]
punch_in_noon_start = punch_in_noon.split(', ')[0]
punch_in_noon_end = punch_in_noon.split(', ')[1]
punch_out_noon_start = punch_out_noon.split(', ')[0]
punch_out_noon_end = punch_out_noon.split(', ')[1]
punch_out_afternoon_start = punch_out_afternoon.split(', ')[0]
punch_out_afternoon_end = punch_out_afternoon.split(', ')[1]
