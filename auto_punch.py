from action import *
import datetime
from except_date.except_date import *
from config.config import *
import time
import random

delay_sec = random.randint(1, delay_time)
print(f'程式將在{delay_sec}秒後運行...')
time.sleep(delay_sec)

now_time = datetime.datetime.now().strftime('%H:%M')
today = datetime.datetime.now().strftime('%Y-%m-%d')
today_weekday = datetime.datetime.now().strftime('%A')  # 取得星期幾

if today_weekday != 'Saturday' and today_weekday != 'Sunday':   # 周末不執行
    if today not in except_date_list:                           # 例外日期不執行
        if punch_in_morning_start <= now_time < punch_in_morning_end \
                or punch_in_noon_start <= now_time < punch_in_noon_end:
            login()
            punch_in()
        elif punch_out_noon_start <= now_time <= punch_out_noon_end \
                or punch_out_afternoon_start <= now_time <= punch_out_afternoon_end:
            login()
            punch_out()
        else:
            print('非打卡時段!')
    else:
        print('not the day to execute punch')
else:
    print('today do not need to work')


