# Web Scraper for jobbank.ca 🇨🇦
[Basant Singh](https://www.linkedin.com/in/basantsingh1000/)🦁

A web scraper for collecting job listings from [jobbank.gc.ca](https://www.jobbank.gc.ca) to analyze the Canadian job market in the given Canadain Cities/Provinces.

## Features
1. City-Based Job Collection: Filters job listings by specific city, making it easy to focus on localized job markets.
2. Comprehensive Data Extraction: Collects details like job titles, locations, employers, salary ranges, descriptions, and posting dates.
3. Automated Navigation: Handles dynamic page content and pagination smoothly.
4. Data Storage: Saves scraped data in JSON formats for easy analysis.

## Technologies Used
1. Python for scripting
2. Selenium & BeautifulSoup for web scraping
3. numpy for storing job_ids


## Useage

``` bash
git clone https://github.com/Guggu-Gill/Job_bank_scrapper.git
cd jobbank-scraper
pip install -r requirements.txt
```


Ensure that the city/Province name provided in arguments is valid and matches the options available on [jobbank.gc.ca](https://www.jobbank.gc.ca).

```bash
python scraper.py --city "Alberta" 
```

## Architecture for Data Analysis on AWS

![Blank diagram (3)](https://github.com/user-attachments/assets/d8ad2e56-ba39-4eb8-9701-0fa0c89ced3e)


