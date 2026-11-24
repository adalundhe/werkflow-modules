from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_authorization_code_properties import GlueAuthorizationCodeProperties
from .glue_o_auth2_client_application import GlueOAuth2ClientApplication
from .glue_o_auth2_credentials import GlueOAuth2Credentials


class GlueOAuth2PropertiesInput(BaseModel):
    OAuth2GrantType: Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER', 'REFRESH_TOKEN'] | None = None
    OAuth2ClientApplication: GlueOAuth2ClientApplication | None = None
    TokenUrl: StrictStr | None = None
    TokenUrlParametersMap: dict[StrictStr, StrictStr] | None = None
    AuthorizationCodeProperties: GlueAuthorizationCodeProperties | None = None
    OAuth2Credentials: GlueOAuth2Credentials | None = None
