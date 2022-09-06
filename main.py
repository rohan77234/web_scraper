# importing all the libraries required
from bs4 import BeautifulSoup  # for web scraping
import requests  # to connect to webpage we want to scrape
import sqlite3  # for database and saving scrapped data into it
from datetime import datetime  # for current date and time of execution of code
import csv

# I put here the verge url for scraping
get_page = requests.get("http://theverge.com")
soup = BeautifulSoup(get_page.text, features="html.parser")
# we have connected to page

###### failed attempt
# link = soup.find_all('h2', class_='c-entry-box--compact__title')# finding links of all articles
# # go to page sourse and check every link is enclosed in <a> tag below <h2> and has class'c-entry-box--compact__title'
# url = [x.a['href'] for x in link]
# print(len(url))
#
#
#
# article = soup.find_all('h2', class_='c-entry-box--compact__title') # go to page sourse and check every headline is
# # enclosed in <h2> tag and has class'c-entry-box--compact__title'
# headline = [x.text for x in article]
# print(len(headline))
#
#
# writer_list = soup.find_all("span", class_='c-byline__item')
# author = [x.text.strip('\n') for x in writer_list]
# print((author))
# final_author = []
# for x in author:
#     if '\n' in x:
#         continue
#     elif "September" in x:
#         continue
#     elif "January" in x:
#         continue
#     elif "February" in x:
#         continue
#     elif "March" in x:
#         continue
#     elif "April" in x:
#         continue
#     elif "May" in x:
#         continue
#     elif "June" in x:
#         continue
#     elif "July" in x:
#         continue
#     elif "August" in x:
#         continue
#     elif "October" in x:
#         continue
#     elif "November" in x:
#         continue
#     elif "December" in x:
#         continue
#     elif len(x) == 0:
#         continue
#     else:
#         final_author.append(x)
# final_author = [x for x in author if x != '\n2']
# print(len(final_author))
# for x in author:
#     print((author))
#     if x[0:1] == '':
#         author.remove(x)
#
#
# date_list = soup.find_all('time', class_='c-byline__item')
# date = [x.get('datetime')[:10] for x in date_list]
# print(len(date))

# while len(mon) < len(tue)-1:
#     mon.insert(0, '0')


# csv22 = [['id', 'url', 'headline', 'author', 'date']]


# apple = [x for x in range(len(mon))]
#
# csv22 = [tuple(apple),
#          tuple(tue),
#          tuple(wed),
#          tuple(thu),
#          tuple(mon)]


writer_list = soup.find_all("div", class_='c-entry-box--compact__body')

try:
    with open("idx.txt", 'r') as f:
        id = int(f.read())
except:
    with open("idx.txt", 'x') as f:
        f.write('0')
        id = 0

data = []
for writer in writer_list:

    fields = []
    fields.append(int(id))

    title = writer.select(".c-entry-box--compact__title")[0].get_text()
    url = writer.select(".c-entry-box--compact__title")[0].a['href']

    fields.append(url)
    fields.append(title)

    authors = writer.select(".c-byline__author-name")
    if len(authors) == 0:
        continue
    author_str = ""
    for author in authors:
        author_str = author_str + author.get_text() + "$"

    fields.append(author_str)

    times = writer.select('time.c-byline__item')
    times_str = ""
    for time in times:
        times_str = times_str + datetime.strptime(time.get('datetime'), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d")

    if times_str == "":
        times_str = "NA"
    fields.append(times_str)

    data.append(fields)
    id += 1
    # print(authors/)
# print(writer_list)

with open("idx.txt", 'w') as f:
    f.write(str(id))


date = datetime.now()
date = date.strftime("%d-%m-%Y")
with open(f"{date}_verge.csv", 'w') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(["id", "url", "article", "author", "date"])
    csvwriter.writerows(data)


db = sqlite3.connect('collect_scrape.db')
cur = db.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS scraped_data (id INTEGER PRIMARY KEY, url TEXT, headline TEXT, author TEXT, date TEXT)')
cur.executemany("INSERT INTO scraped_data VALUES(?, ?, ?, ?, ?)", data)
db.commit()


cur.execute("""DELETE FROM scraped_data WHERE id NOT IN (SELECT MIN(id) id FROM scraped_data GROUP BY headline)""",)
res1 = cur.execute("""select * from scraped_data""")
db.commit()


res = cur.execute("SELECT * FROM scraped_data")
print(len(res.fetchall()))
# print(res)
