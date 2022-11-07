from requests_toolbelt.multipart import decoder
from http.server import BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_POST(self):
        self.path = '/upload'
        content_length = int(self.headers['Content-Length'])

        #get data content bytes
        file_content = self.rfile.read(content_length)

        #Use multipart parser to strip boundary
        multipart_data = decoder.MultipartDecoder(file_content, self.headers['Content-Type']).parts
        image_byte = multipart_data[0].content
        #Read image using cv2
        image_numpy = np.frombuffer(image_byte, np.int8)
        img = cv2.imdecode(image_numpy, cv2.IMREAD_UNCHANGED)

        #Send response
        response = bytes('Message: Successesesese', 'utf-8')
        self.send_response(200) #create header
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)