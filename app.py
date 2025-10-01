from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Kubernetes!</h1>")

if __name__ == "__main__":
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("🚀 Serving on http://localhost:8080 ...")
    httpd.serve_forever()