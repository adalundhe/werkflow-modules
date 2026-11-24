from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .glue_basic_authentication_properties import GlueBasicAuthenticationProperties
from .glue_connector_o_auth2_properties import GlueConnectorOAuth2Properties
from .glue_custom_authentication_properties import GlueCustomAuthenticationProperties


class GlueConnectorAuthenticationConfiguration(BaseModel):
    AuthenticationTypes: list[Literal['BASIC', 'OAUTH2', 'CUSTOM', 'IAM']]
    OAuth2Properties: GlueConnectorOAuth2Properties | None = None
    BasicAuthenticationProperties: GlueBasicAuthenticationProperties | None = None
    CustomAuthenticationProperties: GlueCustomAuthenticationProperties | None = None
