import wsgiserver

class Server: # Main server class with all pages in
    def __init__(self, user, passwd):
        self.user = user # Used for private
        self.passwd = passwd # Used for private

    def main(self, environ, start_response): # Main page
        body = b"Hello world!" # This is the content of the page
        status = '200 OK' # This is the response status code
        headers = [("Content-type", "text/plain")] # Web page headers
        start_response(status, headers) # No idea what this does, but it is required
        yield body # Yield whatever is in the body (i.e. the content of the page)

    def request(self, environ, start_response): # Request page
        address = environ["REMOTE_ADDR"] # Get the IP address of the client
        arg = environ["PATH_INFO"][1:] # Get the path of the request
        method = environ["REQUEST_METHOD"] # Get the method of the request (i.e. POST or GET)
        body = b"Success" # This is the content of the page
        status = '200 OK' # This is the response status code
        headers = [("Content-type", "text/plain")] # Web page headers
        start_response(status, headers) # No idea what this does, but it is required
        yield body # Yield whatever is in the body (i.e. the content of the page)

    def private(self, envrion, start_response): # Private page
        address = envrion["REMOTE_ADDR"] # Get the IP address of the client
        arg = envrion["PATH_INFO"][1:] # Get the path of the request 
        method = envrion["REQUEST_METHOD"] # Get the method of the request (i.e. POST or GET)
        name, pw = arg.split("/")[0:2] # Get the username and password from the request
        if name.upper() == self.user and pw == self.passwd: # Check if the username and password are correct
            body = b"Success:<INSERT PRIVATE DATA HERE>" # This is the content of the page. Could then split at : to access specific data
            status = '200 OK' # This is the response status code
            headers = [("Content-type", "text/plain")] # Web page headers
            start_response(status, headers) # No idea what this does, but it is required
            yield body # Yield whatever is in the body (i.e. the content of the page)
        else: # If the username and password are incorrect
            body = b"Forbidden" # This is the content of the page
            status = '401 Unauthorized' # This is the response status code
            headers = [("Content-type", "text/plain")] # Web page headers
            start_response(status, headers) # No idea what this does, but it is required
            yield body # Yield whatever is in the body (i.e. the content of the page)
    
ServerClass = Server("TEST_USER", "123") # Create a server object with username and password as parameters

d = wsgiserver.WSGIPathInfoDispatcher({ # Create a dictionary of the pages and functions relating to them
            "/": ServerClass.main,
            "/request": ServerClass.request,
            "/private": ServerClass.private,
            })

server = wsgiserver.WSGIServer(d, port=8000) # Create a server object with the dictionary of pages and functions (port is optional. Defaults to 8080)
server.start() # Start the server
