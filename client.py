import http.client

class Response: # Class for the response object
    def __init__(self, status, content): 
        self.status = status # Status code
        self.content = content # Content of the response

def request(method, baseurl, path, timeout): # Function for the request
    conn = http.client.HTTPConnection(baseurl, timeout=timeout) # Create a connection to the server
    conn.request(method,path) # Send the request
    r1 = conn.getresponse() # Get the response
    content = r1.read() # Read the response
    conn.close() # Close the connection
    return Response(r1.status, str(content)[2:-1] ) # Return the response object



def get_data(method, baseurl, path, timeout=10): 
    '''
    method: "POST" or "GET"
    baseurl: "http://www.example.com" or "localhost:8000"
    path: "/path/to/page/POST/DATA"

    '''
    response = request(method, baseurl, path, timeout) # Get the response
    return response.content # Return the content of the response

print(get_data("POST", "localhost:8000", "/private/TEST_USER/123")) # Uses POST request to "localhost:8000/private" with username "TEST_USER" and password "123" as POST data