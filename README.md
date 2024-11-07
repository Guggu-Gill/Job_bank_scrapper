# Job Bank Scraper for jobbank.ca 🇨🇦
[Basant Singh](https://www.linkedin.com/in/basantsingh1000/)🦁

A web scraper for collecting job listings from [jobbank.ca](https://www.jobbank.gc.ca) to analyze the Canadian job market with ease.

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


Ensure that the city name provided in arguments is valid and matches the options available on jobbank.ca.

```bash
python scraper.py --city "Calgary" 
```

## Architecture for Data Analysis on AWS
- dm for code


![Blank diagram (2)](https://github.com/user-attachments/assets/de3384d7-3d9e-4eb4-bb95-5f8e2862586a)


