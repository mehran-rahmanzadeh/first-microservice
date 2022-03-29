from re import T
from django.conf import settings

from users import auth_pb2, auth_pb2_grpc

from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import UntypedToken

import grpc

if api_settings.BLACKLIST_AFTER_ROTATION:
    from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

class AuthServicer(auth_pb2_grpc.AuthControllerServicer):
    """
    Auth Servicer (verify token)
    """

    def VerifyToken(self, request, context):
        token = UntypedToken(request.token)

        if (
            api_settings.BLACKLIST_AFTER_ROTATION
            and "rest_framework_simplejwt.token_blacklist" in settings.INSTALLED_APPS
        ):
            jti = token.get(api_settings.JTI_CLAIM)
            if BlacklistedToken.objects.filter(token__jti=jti).exists():
                context.set_code(grpc.StatusCode.PERMISSION_DENIED)
                return auth_pb2.VerifyResponse(access=False)
        
        context.set_code(grpc.StatusCode.OK)
        return auth_pb2.VerifyResponse(access=True)