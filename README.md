# Web_Scraping-Custom_Search_Engine
Web scraping task to extract data from query results in Googles Custom Search Engine (CSE). The links are results of search queries for different science equipments, company name, company's url and equipment description. The query results are from Googles Custom Search Engine (CSE) which can only be scraped using Google Developer's API_KEY and Requests. Using other scraping software as BeautifulSoup or Scrapy will run into a _reCAPTCHA_ security error.

The results expected:
1. Scrape the following data:
	- Company Name
	- url
	- description
2. Extracted data saved in a CSV file.

# Approach
There are 52 links, each link having 10 pages, and each page having 10 results. The script was developed to loop through each item, extracting the required data, appending them into a dictionary, which later was transformed into a dataframe and saved as a CSV file.

>NOTE: The Developers API_KEY has a free version that only runs 100 queries per day, but can be upgraded to a paid version. The _SEARCH_ENGINE_ID_ is obtained from the link and labelled as **cx**.
