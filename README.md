# Google-search-scrape

This script is using Selenium and Chrome driver to scrape Google's paid search results based on keywords. 

Users input keywords under a column in an Excel Spreadsheet and the script is emulating both mobile and desktop while scraping the results for each.  

Each Google result contains position, a look-up for the company, landing page URL and the copy of the ad as well as if it is Mobile or Desktop.  

The code is cleaning cookies and operating in Chrome Incognito mode.  

The final data output is pushed into a MySQL DB. Once in the DB you can build visualisations using a business intelligence tool such as Microsoft Power BI. 

This script runs for 5 minutes intervals and with 10 keywords. More keywords and in a higher frequency that I would suggest investigating running multiple instances of the Chrome driver.

Input.csv: You add the keywords you want to search there
g-scrape.py: Is the file you will need to run to perform the search and scraping
Output: Is the folder which contains the output of the scrape in a CSV

!!! I have kept the last output as an example 
