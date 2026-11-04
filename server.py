import http.server
import json
import os

PORT = 8080
DIRECTORY = "/data/data/com.termux/files/home/dua-app"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_POST(self):
        print(f"POST request received for path: {self.path}")
        if 'api/save' in self.path:
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                payload = json.loads(post_data.decode('utf-8'))

                lang = 'ms'
                if isinstance(payload, dict) and 'data' in payload:
                    data = payload['data']
                    lang = payload.get('lang', 'ms')
                else:
                    data = payload

                filename = 'duas.json'
                if lang == 'en': filename = 'en-duas.json'
                elif lang == 'cn': filename = 'cn-duas.json'
                elif lang == 'ta': filename = 'ta-duas.json'

                file_path = os.path.join(DIRECTORY, filename)
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)

                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": True, "message": f"Berjaya disimpan ke {filename}!"}).encode('utf-8'))
                print(f"{filename} successfully updated.")
            except Exception as e:
                print(f"Error saving files: {e}")
                self.send_response(500)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, CustomHandler)
    print(f"Serving HTTP on port {PORT} with per-language admin save support...")
    httpd.serve_forever()
