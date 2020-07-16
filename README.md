# google-search-scrape

This script is using Selenium and Chrome driver to scrape Google's paid search results based on keywords. 

The users are inputting their keywords under a column in an Excel Spreadsheet and the script is emulating both mobile and desktop while scraping the results for each.  

Each Google result contains position, a look-up for the company, landing page URL and the copy of the ad as well as if it is Mobile or Desktop.  

The code is cleaning cookies and operating in Icognito mode.  

The final data output is pushed into a MySQL DB and in my project I visualise it in Power BI. 

This script runs well for 5 minutes intervals and with 10 keywords. More that that I would suggest investigating running multiple instances of the Chrome driver.


Input.csv: You add the keywords you want to search there
g-scrape.py: Is the file you will need to run to perform the search and scraping
Output: Is the folder which contains the output of the scrape in a CSV

!!! I have kept the last output as an example 
