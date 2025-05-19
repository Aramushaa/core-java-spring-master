from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class TempRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            payload = json.loads(post_data)
            temperature = payload.get("temperature")
            sensor_id = payload.get("sensor_id")
            print(f"[📥 RECEIVED] Temperature: {temperature}°C from sensor: {sensor_id}")
            self.send_response(200)
        except json.JSONDecodeError:
            print("[❌] Invalid JSON received.")
            self.send_response(400)
        self.end_headers()

    def do_GET(self):
        self.send_error(501, "GET method not supported.")

if __name__ == "__main__":
    server_address = ("localhost", 8083)
    httpd = HTTPServer(server_address, TempRequestHandler)
    print("[🌐] Subscriber running on http://localhost:8083")
    httpd.serve_forever()
