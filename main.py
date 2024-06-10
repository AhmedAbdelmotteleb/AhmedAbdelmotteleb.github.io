import logging
import logging.handlers
import os

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"

def scrape_lhcb():
    url = "https://lhcb-outreach.web.cern.ch/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_div = soup.find('div', class_='mg-latest-news-slider marquee')
    headlines = []
    for i, headline in enumerate(news_div.find_all('a'), 1):
        headline_text = headline.text
        headline_url = headline.get('href')  # extract the URL
        headlines.append((headline_text, headline_url))  # store as a tuple

    with open('headlines.txt', 'w') as f:
        for headline_text, headline_url in headlines:
            f.write(f"{headline_text}\n{headline_url}\n")  # write both the headline and the URL

if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")
    scrape_lhcb()
