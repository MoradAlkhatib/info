from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_http_cat = "https://http.cat/"

        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "status" in dic:
            r = requests.get(url_http_cat+dic['status'])
            data =r
            message ="hello"
            # self.rfile.read(data)
         

        else :
            data = "hi"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(data.encode())
        self.wfile.write(data)
        self.wfile.write(message.encode())
        return

