from django.db import models
import urllib.request
import xml.dom.minidom


def get_data(xml_url):
    web_file = urllib.request.urlopen(xml_url)
    return web_file.read()


def get_value(xml_content):
    domtree = xml.dom.minidom.parse('C:/Users/Ильяс/OneDrive/Рабочий стол/DjangoProject/encomercproject/scriptss/value.xml')
    value = domtree.documentElement
    valuta = value.getElementsByTagName('Valute')
    valut_dict = {}

    for node in valuta:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        valut_dict[char_code] = value
    return valut_dict


def print_dict_for_usd(dict):
    for key in dict.keys():
        if key == 'USD':

            return key


def print_dict_for_eur(dict):
    for key in dict.keys():
        if key == 'EUR':

            return key


def print_dict_values_for_usd(dict):
    for key in dict.keys():
        if key == 'USD':

            return dict[key]


def print_dict_values_for_eur(dict):
    for key in dict.keys():
        if key == 'EUR':

            return dict[key]


url = 'http://www.cbr.ru/scripts/XML_daily.asp'
data = get_value(get_data(url))
data_key_usd = print_dict_for_usd(data)
data_key_eur = print_dict_for_eur(data)
data_value_usd = print_dict_values_for_usd(data)
data_value_eur = print_dict_values_for_eur(data)

