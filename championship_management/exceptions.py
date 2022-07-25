from rest_framework import status, exceptions

class HTTPException(exceptions.APIException):
    
    def __init__(self, detail, status_code=status.HTTP_400_BAD_REQUEST):
        self.detail = detail
        self.status_code = status_code
