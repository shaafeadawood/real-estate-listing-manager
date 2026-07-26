from storage import save_listings

def add_listing(listings):
    address = input("Enter property address: ")
    price = float(input("Enter price: "))
    location = input("Enter city/area: ")
    listing = {
        "address": address,
        "price": price,
        "location": location,
        "status": "available"
    }
    listings.append(listing)
    save_listings(listings)
    print(f"Listing added: {address}")