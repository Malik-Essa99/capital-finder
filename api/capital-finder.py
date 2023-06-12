from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_path = self.path
        url_components = parse.urlsplit(url_path)
        query_list = parse.parse_qsl(url_components.query)
        my_dict = dict(query_list)
        print(my_dict)
        if 'country' in my_dict:
            country = my_dict.get('country')
            country_url = f"https://restcountries.com/v3.1/name/{country}"

            params = {'country': country}
            res = requests.get(country_url, params=params)
            data = res.json()

            for country_info in data:
                capital = country_info["capital"][0]
                message = f"The capital of {country} is {capital}"

        if 'capital' in my_dict:
            capital = my_dict.get('capital')
            capital_url = f"https://restcountries.com/v3.1/capital/{capital}"

            params = {'capital': capital}
            res = requests.get(capital_url, params = params)
            data = res.json()

            for capital_info in data:
                country = capital_info["name"]["common"]
                message = f"{capital} is the capital of {country}"
                
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return
