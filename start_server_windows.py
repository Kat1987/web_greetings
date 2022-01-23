from http import server
import http
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("",8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever ()