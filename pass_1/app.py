from http.server import BaseHTTPRequestHandler, HTTPServer
import random

# Global toggle so we can simulate failure
healthy = True

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global healthy

        if self.path == "/healthz":
            if healthy:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b"OK")
            else:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(b"FAIL")
        elif self.path == "/fail":
            healthy = False
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"App is now unhealthy!")
        elif self.path == "/recover":
            healthy = True
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"App is now healthy again!")
        elif self.path == "/":
            # Simulate “doing work” → add 10k random numbers
            numbers = [random.randint(1, 100) for _ in range(10000)]
            result = sum(numbers)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Sum of 10k random numbers: {result}".encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving on http://localhost:8080 ...")
    httpd.serve_forever()

# import random
# from http.server import SimpleHTTPRequestHandler, HTTPServer

# class HelloHandler(SimpleHTTPRequestHandler):
#     def do_GET(self):
#         # Generate 10,000 random numbers and sum them up
#         numbers = [random.randint(1, 100) for _ in range(10000)]
#         total = sum(numbers)

#         # Build response HTML
#         response = f"""
#         <html>
#             <head><title>Random Number Factory</title></head>
#             <body>
#                 <h1>Hello from Docker!</h1>
#                 <p>I just generated 10,000 random numbers and summed them up.</p>
#                 <p><b>Total:</b> {total}</p>
#             </body>
#         </html>
#         """

#         # Send response headers
#         self.send_response(200)
#         self.send_header("Content-type", "text/html")
#         self.end_headers()

#         # Write response body
#         self.wfile.write(response.encode("utf-8"))

# if __name__ == "__main__":
#     # Run server on port 8080
#     server_address = ("", 8080)
#     httpd = HTTPServer(server_address, HelloHandler)
#     print("Serving on http://localhost:8080 ...")
#     httpd.serve_forever()