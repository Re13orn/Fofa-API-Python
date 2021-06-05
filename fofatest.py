import pyfofa
import time
import csv
import pandas as pd
import os
import sys
start=time.time()
bar_len = 60
logo="""

 ██████╗██╗   ██╗██████╗ ███████╗██████╗     ██╗    ██╗ █████╗ ██████╗ ███████╗ █████╗ ██████╗ ███████╗
██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██║    ██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝
██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ██║ █╗ ██║███████║██████╔╝█████╗  ███████║██████╔╝█████╗  
██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██║███╗██║██╔══██║██╔══██╗██╔══╝  ██╔══██║██╔══██╗██╔══╝  
╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ╚███╔███╔╝██║  ██║██║  ██║██║     ██║  ██║██║  ██║███████╗
 ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                                                                                  Author:Ren   Ver:1.0
"""
print(logo)
def search():
    email = ''
    key = ''
    search = pyfofa.FofaAPI(email, key)
    try:
        test = search.get_data("123456")['size']
    except:
        print('請檢查Email及Key是否輸入正確')
        exit(1)
    search_fofa = input("\n請輸入關鍵字 :")
    keyword = str(search_fofa).split("\"")
    if len(keyword) > 1:
        f = open("./output/%s_%s.csv"%(keyword[1],time.strftime("%m月%d日%H%M", time.localtime())),'w',encoding='utf-8',newline='')
    else:
        f = open("./output/%s_%s.txt"%(search_fofa,time.strftime("%m月%d日%H%M", time.localtime())),'w',encoding='utf-8',newline='')
    try:
        size = search.get_data(search_fofa)['size']
        pagenum = int(size/100 + 1)
        print("\n共%s筆，共%s頁\n"%(size,pagenum))
        name = ['Url','Title','Country','City','IP','Port','Server','Protocol'] #csv表格列
        writer = csv.writer(f)
        writer.writerow(name)
        print("請稍候，爬取中")
        for page in range(1,pagenum):
            re_date = search.get_data(search_fofa, page, "host,title,country_name,city,ip,port,server,protocol")['results']
            writer.writerows(re_date)
            filled_len = int(round(bar_len * (page+1) / float(pagenum)))
            percents = round(100.0 * (page+1) / float(pagenum), 1)
            bar = ['='] * filled_len + ['-'] * (bar_len - filled_len)
            sys.stdout.write('[%s] %s%s %s/%s頁\r' % (''.join(bar), percents, '%', page, pagenum))
            sys.stdout.flush()
            # print("第%s頁，共%s頁"%(page,pagenum))
        print("\n!!完成!!")
    except:
        print("請檢查關鍵字是否正確")
search()
end = time.time()
sd = end-start
lj = os.path.dirname(__file__)
print('\n資料保存在:'+lj + '\\output目錄下面')
print('\n耗費:%s秒'%round(sd))