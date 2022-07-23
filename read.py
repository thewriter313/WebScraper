from write import export
from bs4 import BeautifulSoup
import requests
import numpy as np

def read():
    url = 'https://catalog.febest.eu/?limit=100&manufacturer=51&model=1737&page=2'

    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'lxml')
    parts = soup.find_all('article', class_ = 'ArticleListItem_article__1inS5')
    names = np.array([])
    numbers = np.array([])

    for part in parts:

        item_name = part.find('h4').text

        item_numbers_raw = part.find_all('div', class_ = 'ArticleListItem_articleOemInfoTextWrapper__209EJ')

        items = []
        for item_number_raw in item_numbers_raw:

            item_number = item_number_raw.text
            if 'HONDA:' in item_number:
                if item_number == '...':
                    pass
                else:
                    items.append(item_number)
            
        items = items[:2]
        item_single = ''
        if not items:
            item_single = '-'
        else:
            if len(items) > 1:
                item_single = items[0] + ' | ' + items[1]
            else:
                item_single = items[0]
            
        names = np.append(names, item_name).transpose()
        
        numbers = np.append(numbers, item_single)
    print(names.shape)
    print(numbers.shape)
    dataframe = np.column_stack((names, numbers))
    print(dataframe.shape)
    export(dataframe)

