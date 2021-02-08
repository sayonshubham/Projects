# 1. Import the necessary LIBRARIES
import requests
from bs4 import BeautifulSoup
import numpy as np
import csv

# 2. Create a User Agent (Optional)
headers = {"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                         "KHTML, like Gecko) Version/4.0 Safari/534.30"}

# 3. Send get() Request and fetch the webpage contents
response = requests.get('https://stackoverflow.com/questions/tagged/python?tab=votes&page=1&pagesize=50',
                        headers=headers)
webpage = response.content
# 4. Check Status Code (Optional)
# print(response.status_code)

# 5. Create a Beautiful Soup Object
soup = BeautifulSoup(webpage, "html.parser")
# print(soup.prettify())

# 6. The Logic
with open("topics.csv", "a") as csv_file:
    writer = csv.writer(csv_file)
    for parent in soup.find_all('div', class_='-details'):
        topic = [t for t in parent.find_all('h2')]
        for item in topic:
            title=item.text.strip()
            print(title)
            writer.writerow([title])


        # loop to next 4 pages
    pages = np.arange(2, 6, 1)
    for page in pages:
        link = "https://stackoverflow.com/questions/tagged/python?tab=votes&page=" + str(page)

        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 ("
                          "KHTML, like Gecko) Version/4.0 Safari/534.30"}
        res = requests.get(link)
        web_page = res.content
        soup_2 = BeautifulSoup(web_page, "html.parser")
        for parent in soup_2.find_all('div', class_='summary'):
            topic = [t for t in parent.find_all('h3')]
            for item in topic:
                t = item.text.strip()
                print(t)
                writer.writerow([t])
