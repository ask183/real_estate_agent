import os
from crewai_tools import ScrapegraphScrapeTool

def scrape_listings(city="Austin", state="TX"):
    scrape_tool = ScrapegraphScrapeTool()
    url = f"https://www.zillow.com/homes/for_sale/{city}-{state}/"
    prompt = (
        "Extract each property with price, number of bedrooms, bathrooms, "
        "square footage, and listing URL."
    )
    listings = scrape_tool.run(website_url=url, prompt=prompt)
    return listings