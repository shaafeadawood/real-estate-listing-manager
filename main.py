from storage import load_listings
from features.add_listing import add_listing
from features.filter_listings import filter_listings

def show_menu():
    print("\n--- Real Estate Listing Manager ---")
    print("1. Add a new listing")
    print("2. Filter listings")
    print("3. Exit")

def main():
    listings = load_listings()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_listing(listings)
        elif choice == "2":
            filter_listings(listings)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()