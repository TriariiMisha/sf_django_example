import logging
from http import HTTPStatus

from rest_framework.exceptions import APIException
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

logger = logging.getLogger(__name__)


class BaseException(APIException):
    status_code = HTTPStatus.NO_CONTENT


class AuthRequiredError(BaseException):
    status_code = HTTP_401_UNAUTHORIZED
    default_detail = 'Authentication required'


class BadRequestException(BaseException):
    status_code = HTTP_400_BAD_REQUEST
    default_detail = 'bad request'
    default_code = 'bad_request'


class SerializationException(BaseException):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "server error"
    default_code = "server error"


class ServerException(BaseException):
    status_code = HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'server error'
    default_code = 'server error'


class ResourceForbiddenException(BaseException):
    status_code = HTTP_403_FORBIDDEN
    default_detail = 'no access to provided resource'
    default_code = 'resource_forbidden_error'


class ResourceNotFoundException(BaseException):
    status_code = HTTP_404_NOT_FOUND
    default_detail = 'resource_not_found'
    default_code = 'not_found'
