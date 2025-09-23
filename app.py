import random
from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Generate 10,000 random numbers and sum them up
        numbers = [random.randint(1, 100) for _ in range(10000)]
        total = sum(numbers)

        # Build response HTML
        response = f"""
        <html>
            <head><title>Random Number Factory</title></head>
            <body>
                <h1>Hello from Docker!</h1>
                <p>I just generated 10,000 random numbers and summed them up.</p>
                <p><b>Total:</b> {total}</p>
            </body>
        </html>
        """

        # Send response headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Write response body
        self.wfile.write(response.encode("utf-8"))

if __name__ == "__main__":
    # Run server on port 8080
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving on http://localhost:8080 ...")
    httpd.serve_forever()