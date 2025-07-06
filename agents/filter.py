import json

def load_filters():
    with open('user_filters/filters.json') as f:
        return json.load(f)

def filter_listings(listings):
    filters = load_filters()
    filtered = []
    for listing in listings:
        try:
            if (filters['min_price'] <= listing['price'] <= filters['max_price'] and
                filters['min_beds'] <= listing['beds'] <= filters['max_beds'] and
                filters['min_sqft'] <= listing['sqft'] <= filters['max_sqft']):
                filtered.append(listing)
        except KeyError:
            continue
    return filtered