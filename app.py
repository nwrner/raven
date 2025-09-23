from http.server import SimpleHTTPRequestHandler, HTTPServer

class HelloHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Always respond with 200 OK
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Write the hello world response
        self.wfile.write(b"Hello world but from Docker! :)")

if __name__ == "__main__":
    # Run server on port 8080
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, HelloHandler)
    print("Serving on http://localhost:8080 ...")
    httpd.serve_forever()
