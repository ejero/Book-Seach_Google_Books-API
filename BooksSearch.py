__author__ = 'Rosita Emakpo'

import credentials
from googleapiclient.discovery import build

# Build the Google Books API service
service = build('books', 'v1', developerKey=credentials.API_KEY)

# This will be the reading list. We will add to it every time the user searches.
reading_list = []

def search_and_display_books():
    while True:
        search_query = input("Enter book search query (or type 'exit' to quit): ").strip()
        if search_query.lower() == 'exit':
            break

        # Check if search query is blank
        while not search_query:
            search_query = input("Search query cannot be blank: ").strip()

        try:
            # Do the search
            search = service.volumes().list(q=search_query)
            response = search.execute()
            items = response.get('items', [])

            if not items:
                print("No books found for this query.\n")
                continue

            # Display the top 5 items
            print("\nTop results:")
            for i, item in enumerate(items[:5]):
                vol = item.get('volumeInfo', {})
                title = vol.get('title', 'Unknown Title')
                authors = vol.get('authors', [])
                publisher = vol.get('publisher', 'Unknown Publisher')
                print(f"{i + 1}. {title} by {', '.join(authors) if authors else 'Unknown Author'}")
                print(f"\tpublished by {publisher}")

            # Ask the user which book to add to the reading list
            print('\nType the number of the book to add to your reading list, or 0 to skip.')
            try:
                selection = int(input("Your choice: "))
                if selection == 0:
                    continue
                if 1 <= selection <= min(5, len(items)):
                    selected_item = items[selection - 1].get('volumeInfo', {})
                    reading_list.append({
                        'title': selected_item.get('title', 'Unknown Title'),
                        'authors': selected_item.get('authors', []),
                        'publisher': selected_item.get('publisher', 'Unknown Publisher')
                    })
                    print(f"Added '{selected_item.get('title', 'Unknown Title')}' to your reading list!\n")
                else:
                    print("Invalid selection. Please try again.\n")
            except ValueError:
                print("Please enter a valid number.\n")
        except Exception as e:
            print(f"An error occurred during the search: {e}\n")

def show_reading_list():
    search_and_display_books()
    print("\nHere is your reading list:")
    if not reading_list:
        print("Your reading list is empty.")
    for item in reading_list:
        title = item['title']
        authors = ', '.join(item['authors']) if item['authors'] else 'Unknown Author'
        publisher = item['publisher']
        print(f"{title} by {authors}")
        print(f"\tpublished by {publisher}")

if __name__ == "__main__":
    show_reading_list()
