# BooksSearch
BooksSeach.py is a Python project that uses Google Books API 

## Installation
There are a couple things you will need in order to properly run this app.
- Google Client API
- Python 3.4 or newer

### Mac/Linux
```bash
pip install virtualenv
virtualenv <your-env>
source <your-env>/bin/activate
<your-env>/bin/pip install google-api-python-client
```

### Windows 
```bash
pip install virtualenv
virtualenv <your-env>
<your-env>\Scripts\activate
<your-env>\Scripts\pip.exe install google-api-python-client
```
## Usage

Open the project in your IDE of choice (I used pyCharm CE) Press the green play button to run the program and in the console enter a search query. Five books will be displayed. Choose a book to add to your reading list by typing any number between 1 - 5. Once you are done searching type 'exit' to end the program. 

Google Books API documentation can be viewed [here](https://developers.google.com/books). 
