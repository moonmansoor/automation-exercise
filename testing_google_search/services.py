import re
import requests
from bs4 import BeautifulSoup


def get_google_search_result(keywords, num_of_result=5):
    google_url = "https://www.google.com/search?q=" + keywords
    response = requests.get(google_url)
    soup = BeautifulSoup(response.text, "html.parser")

    result_div = soup.find_all('div', attrs={'class': 'ZINbbc'})

    links = []
    titles = []
    for index, result in enumerate(result_div):
        if result and result.find('div', attrs={'class': 'vvjwJb'}):
            link_href = result.find('a', href=re.compile(r"[/]([a-z]|[A-Z])\w+")).attrs['href']
            link = link_href.replace('/url?q=', '')
            title = result.find('div', attrs={'class': 'vvjwJb'}).get_text()
        else:
            link = '-'
            title = 'No search result'

        # Check to make sure everything is present before appending
        if link != '' and title != '':
            links.append(link)
            titles.append(title)

        if index == num_of_result:
            break

    # clean_links = list(set(links))
    # clean_titles = list(set(titles))

    for index, title in enumerate(titles):
        for index_2, link in enumerate(links):
            if index == index_2:
                # show the result
                print(f'{index+1}:{title}, {link}' + '\n')
