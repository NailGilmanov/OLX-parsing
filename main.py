import requests
from bs4 import BeautifulSoup

# Я для теста выбрал категорию элеткроника/компьютеры (Узбекистан)
main_url = 'https://www.olx.uz/d/elektronika/kompyutery/'
country = 'uz'

# Количество товаров в подборке
amount_of_collestion = 10


def write_result(result):
    for item in result:
        print(item)


def get_page_data(main_url):
    req = requests.get(main_url)
    soup = BeautifulSoup(req.content, "html.parser")
    table = soup.find('div', {'class': 'listing-grid-container'})
    rows = table.find_all('div', {"data-cy": 'l-card'})

    result = []
    for i in range(amount_of_collestion):
        name = rows[i].find('h6').text
        url = main_url[:-1] + rows[i].find('a').get('href')
        price = rows[i].find('p', {"data-testid": "ad-price"}).text
        address = rows[i].find('p', {"data-testid": "location-date"}).text

        item = {'name': name, 'price': price, 'address': address, "url": url}
        result.append(item)
    return result


def main(main_url):
    result = get_page_data(main_url)
    write_result(result)


if __name__ == '__main__':
    main(main_url)
