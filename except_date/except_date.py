import os

file_path = r"D:\Python\auto_punch_in\except_date\except date.txt"

if os.path.isfile(file_path):
    f = open(file_path, encoding='utf-8')

    except_date_list = []
    for line in f.readlines():
        if line.rstrip() != '注意日期格式為"YYYY-mm-dd"' and line.rstrip() != '':
            except_date_list.append(line.rstrip())
    f.close()
else:
    print('File not exist')
