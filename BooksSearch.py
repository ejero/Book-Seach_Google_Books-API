__author__ = 'Rosita Emakpo'
import pprint

# build API
from googleapiclient.discovery import build
API_KEY = "#"
service = build('books', 'v1', developerKey="Enter Your Key here")

# this will be the reading list.
# we will add to it every time he searches.
items = []


def search_and_display_books():
    while True:
        searchQuery = input("Enter book search query: ")
        if searchQuery.strip().lower() == 'exit':
            # if the user types exit stop searching
            break;

        # check if search query is blank
        while searchQuery == '':
            searchQuery = input("Search query can not be blank: ")

        # do the search
        search = service.volumes().list(q=searchQuery)
        response = search.execute()

        # display the top 5 items
        for i, item in enumerate(response['items'][0:5]):
            vol = item['volumeInfo']
            print(i + 1, vol['title'], 'by', ", ".join(vol['authors']))
            print('\tpublished by', vol.get('publisher'))

        # ask the user which book to add to the reading list
        print()
        print('Please type in the number of the book to add to your reading list')
        x = int(input())

        # fetch that item from the json response.
        item = response['items'][x]['volumeInfo']
        # convert the item's structure into the required format and add it to the list
        items.append({'title': vol['title'], 'authors': vol['authors'], 'publisher': vol.get('publisher')})



def show_reading_list():
    search_and_display_books()
    print("Here is your reading list")
    for item in items:
        # this ",".join is needed because the authors is a list and not a single
        # item. the join will join them all together by a comma and display as a
        # single string.
        print(item['title'], 'by', ', '.join(item['authors']))
        print('\tpublished by', item['publisher'])


show_reading_list()
