from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        

        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "amount" in dic:
            url_http_cat = "https://opentdb.com/api.php?amount="
            r = requests.get(url_http_cat+dic['amount'])
            data = r.json()
            message = ""
            if int(dic['amount']) < 51:
                for i in range(int(dic['amount'])):
                    question = data['results'][i]['question']
                    answer = data['results'][i]['correct_answer']
                    message+=f"{question} The Answer Is: {answer}  \n"
            
            else :
                message = "We Can Retrieve 50 Question Maximum."

        elif "category" in dic:
                url_http_cat = "https://opentdb.com/api.php?amount=10&category="
                r = requests.get(url_http_cat+dic['category'])
                data = r.json()
                message = f"{dic['category']}\n"
                for i in range(10):
                    question = data['results'][i]['question']
                    answer = data['results'][i]['correct_answer']
                    message+=f"{question} The Answer Is: {answer}  \n"
                



        else :
            message = "hi"
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
       
       
       
        return

