from action import *
import datetime
from except_date.except_date import *

now_time = datetime.datetime.now().strftime('%H:%M')
today = datetime.datetime.now().strftime('%Y-%m-%d')
today_weekday = datetime.datetime.now().strftime('%A')  # 取得星期幾

if today_weekday != 'Saturday' and today_weekday != 'Sunday':   # 周末不執行
    if today not in except_date_list:                           # 例外日期不執行
        if '07:55' < now_time < '08:00' or '13:25' < now_time < '13:30':
            login()
            punch_in()
        elif '12:00' < now_time < '12:05' or '17:30' < now_time < '17:35':
            login()
            punch_out()
        else:
            print('非打卡時段!')
    else:
        print('not the day to execute punch')
else:
    print('today do not need to work')


