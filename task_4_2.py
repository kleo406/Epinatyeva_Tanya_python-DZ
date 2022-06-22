import requests
URL='http://www.cbr.ru/scripts/XML_daily.asp'
response=requests.get(URL)
data=response.text.split('</Valute>')
money_code_lst=[i[(i.find('<CharCode>')+len('<CharCode>')):i.find('</CharCode>')] for i in data]
nominal_lst=[i[(i.find('<Nominal>')+len('<Nominal>')):i.find('</Nominal')] for i in data]
money_name_lst=[i[(i.find('<Name>')+len('<Name>')):i.find('</Name>')] for i in data]
value_lst=[i[(i.find('<Value>')+len('<Value>')):i.find('</Value>')].replace(',' , '.') for i in data]
def currency_rates(any_money_name):
    try:
        index=money_code_lst.index(any_money_name)
    except ValueError:
        return None
    return f'{money_name_lst[index]} равен {float(value_lst[index])/float(nominal_lst[index])} рублей'
if __name__ == '__main__':
    chse=((input(f'Список валют:\n{money_code_lst}\n Что бы узнать курс, введите код валюты из списка: ')).upper())
print(currency_rates(chse))