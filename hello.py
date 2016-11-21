# A relatively simple WSGI application. It's going to print out the
# environment dictionary after being updated by setup_testing_defaults
def app(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    query = environ["QUERY_STRING"].split('&')
    start_response(status, headers)
    ret = [("%s\n" % (value)).encode("utf-8")
           for value in query]
    return ret

