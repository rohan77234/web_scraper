# web_scraper
scraping headline, url, author, date from a website.

In reference to problem statement given by shack labs on internshala.
as the problem statement stated i have successfully completed all the tasks and
here's how

1. imported all the requited modules in line 1 to 6.
2. using request module successfully connected to theverge.com.
3. used beautifulSoup library to scrape data off the verge.com 
4. then line 11 to 89 contain a unsuccessful attempt, as comment.
5. i created a file to remember last id entered in database
6. data extracted 
7. data saved in csv file with appropriate output.
8. database created and in a table data is saved.
9. duplicate values removed.
10. and tested on github server.


test cases :
1. while extracting data faced many issues as in failed attempt.
as some of articles has multiple authors and was unable to extract them.
2. some of articles did not had date in them and ads was also getting processed.
3. ads were removed but date less articles were left as is.
4. saving data in csv file was done which lead to a new csv file daily as included in zip file.
5. as id was set to primary key it dosent allow duplicte values this problem was tackled by-
-- creating a txt file which saves id of last article in database and reads again at start of -
-- data entering in database see line 92-99 and 35-36
6. Duplicate data removal is also little tricky with sqlite.
7. running the script everyday using crontab is also diffrent in cloud vs your machine(mac in my case).




note: all the tasks were successfully completed but was unable to run code on aws as my account is
facing some issues with verification.
