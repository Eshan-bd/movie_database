import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

logger = logging.getLogger('global_error_logger')

def global_exception_handler(exc, context):
    """
    Global Exception Handler for DRF.
    """
    response = exception_handler(exc, context)

    if response is None:
        logger.error(f"Unhandled Exception: {exc}", exc_info=True)
        return Response(
            {"error": "Something went wrong. Please try again later."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    logger.warning(f"Handled Exception: {response.data}")

    return response