import logging
from flask import Flask, request

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS', 'HEAD'])
def catch_all(path):
    logger.info(f"Received request: {request.method} {request.url}")
    logger.info(f"Headers: {request.headers}")
    logger.info(f"Body: {request.get_data(as_text=True)}")
    return "<html><body><h1>Hello, World!</h1><p>This is a test.</p></body></html>"

if __name__ == '__main__':
    app.run(port=5000)
