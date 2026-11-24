from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .glue_client_credentials_properties import GlueClientCredentialsProperties
from .glue_connector_authorization_code_properties import GlueConnectorAuthorizationCodeProperties
from .glue_jwt_bearer_properties import GlueJWTBearerProperties


class GlueConnectorOAuth2Properties(BaseModel):
    OAuth2GrantType: Literal['CLIENT_CREDENTIALS', 'JWT_BEARER', 'AUTHORIZATION_CODE']
    ClientCredentialsProperties: GlueClientCredentialsProperties | None = None
    JWTBearerProperties: GlueJWTBearerProperties | None = None
    AuthorizationCodeProperties: GlueConnectorAuthorizationCodeProperties | None = None
