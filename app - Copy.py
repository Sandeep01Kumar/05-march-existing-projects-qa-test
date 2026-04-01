from flask import Flask, Response

hostname = '127.0.0.1'
port = 3000

app = Flask(__name__, static_folder=None)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'])
def catch_all(path):
    return Response('Hello, World!\n', status=200, content_type='text/plain')


@app.errorhandler(405)
def method_not_allowed(e):
    return Response('Hello, World!\n', status=200, content_type='text/plain')


if __name__ == '__main__':
    print(f'Server running at http://{hostname}:{port}/')
    app.run(host=hostname, port=port)
