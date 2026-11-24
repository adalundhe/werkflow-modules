from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_o_auth2_properties import GlueOAuth2Properties


class GlueAuthenticationConfiguration(BaseModel):
    AuthenticationType: StrictStr | None = None
    SecretArn: StrictStr | None = None
    KmsKeyArn: StrictStr | None = None
    OAuth2Properties: GlueOAuth2Properties | None = None
