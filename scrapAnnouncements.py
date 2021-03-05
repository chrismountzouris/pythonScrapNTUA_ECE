import requests
import re
from bs4 import BeautifulSoup

page = requests.get("http://mycourses.ntua.gr/announcements/announcements.php?cidReq=PSTGR1083")

soup = BeautifulSoup(page.content, 'html.parser')

full_body = soup.find(id="claroBody")

announcement_title = full_body.find_all(class_="coursesubtitle")

announcement_date = full_body.find_all(class_="itemdate")

announcement_p_details = full_body.find_all("p")

full_body_str = str(full_body)

announcement_details = re.findall("<p><p>(.*?)</p></p>", full_body_str)

for i in range (0,10):

    print (announcement_title[i].get_text())

    print (announcement_date[i].get_text())

    announcement_details[i] = announcement_details[i].replace("</p><p>", "\n")

    announcement_details[i] = re.sub('<[^<]+?>', '', announcement_details[i])
    
    print (announcement_details[i])

    print ('--------------------------------')
