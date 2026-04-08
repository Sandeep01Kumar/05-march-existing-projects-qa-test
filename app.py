"""
Flask HTTP server application — replaces the original Node.js server.js.

This module implements a minimal Flask web server that replicates the exact
behavior of the original Node.js HTTP server: it responds to every HTTP request
(any method, any path) with HTTP 200, Content-Type text/plain, and the body
'Hello, World!\n'. The server binds to 127.0.0.1 on port 3000.
"""

from flask import Flask, Response

# Flask application instance
app = Flask(__name__)

# Server configuration constants — match original Node.js server.js values exactly
hostname = '127.0.0.1'
port = 3000


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def catch_all(path):
    """Handle every HTTP request with an identical plain-text response.

    This catch-all route replicates the original Node.js server behavior:
    regardless of the HTTP method or URL path, it returns HTTP 200 with
    Content-Type text/plain and the body 'Hello, World!\n'.

    Args:
        path: The URL path segment captured by the route. Unused — all paths
              receive the same response.

    Returns:
        A Flask Response object with status 200, content_type 'text/plain',
        and body 'Hello, World!\n'.
    """
    return Response('Hello, World!\n', status=200, content_type='text/plain')


if __name__ == '__main__':
    print(f'Server running at http://{hostname}:{port}/')
    app.run(host=hostname, port=port)
