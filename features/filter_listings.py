def filter_listings(listings):
    location = input("Filter by location (leave blank to skip): ").strip()
    max_price_input = input("Max price (leave blank to skip): ").strip()

    results = listings
    if location:
        results = [l for l in results if l["location"].lower() == location.lower()]
    if max_price_input:
        max_price = float(max_price_input)
        results = [l for l in results if l["price"] <= max_price]

    if not results:
        print("No matching listings found.")
    for l in results:
        print(f"{l['address']} | {l['location']} | ${l['price']} | {l['status']}")
