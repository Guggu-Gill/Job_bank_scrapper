# Job Bank Scraper for jobbank.ca 🇨🇦
[Basant Singh](https://www.linkedin.com/in/basantsingh1000/)🦁

A web scraper for collecting job listings from jobbank.ca to analyze the Canadian job market with ease. It stores data into local disk.

## Features
1. City-Based Job Collection: Filters job listings by specific city, making it easy to focus on localized job markets.
2. Comprehensive Data Extraction: Collects details like job titles, locations, employers, salary ranges, descriptions, and posting dates.
3. Automated Navigation: Handles dynamic page content and pagination smoothly.
4. Data Storage: Saves scraped data in JSON formats for easy analysis.

## Technologies Used
1. Python for scripting
2. Selenium & BeautifulSoup for web scraping
3. numpy for storing job_id




``python
# City name must be valid
# do verify valid city name on jobbank.ca
python scraper.py --city "Toronto" 
``
