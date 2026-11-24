from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_basic_authentication_credentials import GlueBasicAuthenticationCredentials
from .glue_o_auth2_properties_input import GlueOAuth2PropertiesInput


class GlueAuthenticationConfigurationInput(BaseModel):
    AuthenticationType: Literal['BASIC', 'OAUTH2', 'CUSTOM', 'IAM'] | None = None
    OAuth2Properties: GlueOAuth2PropertiesInput | None = None
    SecretArn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    BasicAuthenticationCredentials: GlueBasicAuthenticationCredentials | None = None
    CustomAuthenticationCredentials: dict[StrictStr, StrictStr] | None = None
