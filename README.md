# WebScraper Demo

This is a demo for web scraping websites using the Scrapy library in Python. It includes two types of spiders for different web scraping tasks.

## Installation

To install Scrapy, you can use pip:

```bash
pip install scrapy
```
Tip: You can use a Virtual Environment for the installation

## Running the Scraper

```bash
scrapy crawl [SpiderName]
```

Replace [SpiderName] with the name of any spider available in the Spiders folder.

## Configuration

You can configure the output format and file location in the **settings.py** file. Here are the relevant settings:

```py

# Example settings for output format and file location
FEED_FORMAT = 'csv'
FEED_URI = 'output.csv'

```

You can change FEED_FORMAT to any supported format such as json, xml, etc., and FEED_URI to the desired output file path.


## Additional Resources

* [Scrapy Documentation](https://docs.scrapy.org/en/latest/)

* [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html)
