# run with `gunicorn server:app` under CPython 3.10

DATA = b'Hello, World!\n' * 100

def app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(DATA)))
    ]
    start_response(status, response_headers)
    return iter([DATA])
