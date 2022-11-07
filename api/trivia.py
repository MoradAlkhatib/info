from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_http_cat = "https://opentdb.com/api.php?amount="

        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "amount" in dic:
            r = requests.get(url_http_cat+dic['amount'])
            data = r.json()
            print(data)
            message = data['results'][0]['category']
            
            
         

        else :
            message = "hi"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        self.wfile.write(message.encode())
        self.wfile.write(message.encode())
       
       
        return

