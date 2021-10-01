import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import argparse


def parse_url(link):
    url = urlparse(link)
    netloc = url.netloc
    path = url.path
    parsed_bitlink = f'{netloc}{path}'
    return parsed_bitlink


def is_bitlink(bitly_token, parsed_link):
    headers = {'Authorization': bitly_token}
    checking_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_link}'
    response = requests.get(checking_url, headers=headers)
    return response.ok


def shorten_link(bitly_token, link):
    headers = {'Authorization': bitly_token}
    payload = {'long_url': link}
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    bitly_answer = response.json()
    bitlink = bitly_answer['id']
    return bitlink


def count_clicks(bitly_token, bitlink):
    headers = {'Authorization': bitly_token}
    payload = {'unit': 'day', 'units': '-1'}
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    clicks_url = f'{api_url}{bitlink}/clicks/summary'
    response = requests.get(clicks_url, headers=headers, params=payload)
    response.raise_for_status()
    bitly_answer = response.json()
    clicks_count = bitly_answer['total_clicks']
    return clicks_count


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("link")
    args = parser.parse_args()
    link = args.link
    BITLY_TOKEN = os.environ['bitly_token']
    try:
        parsed_link = parse_url(link)
        if is_bitlink(bitly_token, parsed_link):
            total_clicks = count_clicks(bitly_token, parsed_link)
            print('Это битлинк\n', 'Кол-во кликов', total_clicks)
        else:
            bitlink = shorten_link(bitly_token, link)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError as e:
        print('Введите корректный адрес ссылки')
        raise SystemExit(e)


if __name__ == '__main__':
    main()
