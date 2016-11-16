from wsgiref.util import setup_testing_defaults, application_uri
from wsgiref.simple_server import make_server

# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    query = environ["QUERY_STRING"].split('&')
    start_response(status, headers)
    ret = [("%s\n" % (value)).encode("utf-8")
           for value in query]
    return ret

httpd = make_server('', 8080, simple_app)
print("Serving on port 8080...")
httpd.serve_forever()