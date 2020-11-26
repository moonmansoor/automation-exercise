# Automation Test for Google Search

This is the Automation Exercise for automate
google keyword search.

In this testing I'm using Selenium Webdriver and the test case was written in Python.

`Here how to test it`

1. run `pip install -r requirements.txt`

2. run `pytest test_google_search.py -s`

The search result(Title, URL) will display in the terminal and also in `Search Result.txt` file.

I just add new services `get_google_search_result(keywords, num_of_result)`
Where you can pass the `keyword`. `num_of_result` is default to 5.

You can test in `python shell` and import the services.
```
1. from services import get_google_search_result
2. get_google_search_result('something')
```
