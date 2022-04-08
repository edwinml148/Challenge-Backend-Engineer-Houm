import requests

class RequestError(Exception):
    """
    Attributes:
        status_code -- status code http in the request for url
        message -- explanation of the error

    The reason for the failure of the request.
    """
    def __init__(self, status_code, url, message = "Error in the request for url"):
        self.status_code = status_code
        self.message = message + ": {}".format(url)
        super().__init__(self.message)


def api_response(url) -> dict or str:
    """
    Attributes:
        url -- api consumption address
    Return the response of the api in json format.
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise RequestError(response.status_code, url)