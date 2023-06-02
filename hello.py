import time, os

with open('/var/www/html/index.html','w+') as f:
    f.write("hello")
    
os.remove('/var/www/html/index.nginx-debian.html')

os.system("service nginx start")

while True:
    print("start!")
    time.sleep(2)
