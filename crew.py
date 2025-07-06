from agents.scraper import scrape_listings
from agents.filter import filter_listings
from agents.emailer import send_email
import os
from dotenv import load_dotenv

load_dotenv()

def run_crew():
    listings = scrape_listings()
    filtered = filter_listings(listings)
    send_email(filtered, os.getenv('TO_EMAIL'))

if __name__ == "__main__":
    run_crew()