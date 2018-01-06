import time
from datetime import datetime as dt

hosts_test_path = "hosts"
hosts_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

#dynamic values - can be changed
workingHourStart = 9
workingHourEnd = 18
secondsToRunScript = 300

while True:
    # check time every X minutes - if it's between 8:00 AM to 16:00 PM
    # if it is -> add the website_list to hosts file in the relevant structure
    # else -> remove those lines from the hosts file
    if dt(dt.now().year, dt.now().month, dt.now().day, workingHourStart) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, workingHourEnd):
        print("Working Hours now :(")
        # r+ - appending, unlike 'w' which is write and actually *only* write a new file
        with open(hosts_path, 'r+') as file:
            content = file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" + redirect + " " + website)
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Fun hours :)")
    time.sleep(secondsToRunScript) #every 5 minutes
