import time
from datetime import datetime as dt
host_path = r"C:\Windows\System32\drivers\etc\hosts"
# IF Unix- /etc/hosts
#redirect to a motivational website
redirect = "23.253.54.202"
website_list = ["www.facebook.com", "facebook.com", "yahoo.com"]
while True:
    if dt(dt.now().year,dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+""+ website+"\n")
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any (website in line for website in website_list):
                    file.write(line)
                file.truncate()
    time.sleep(5)

# In windows use Task Scheduler to convert the program into a process and run at startup, running with highest privledges
#In Unix based systems, run sudo crontab -e, then add the line "@reboot python3 <.py filepath>"
