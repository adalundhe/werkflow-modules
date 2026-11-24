from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_property import GlueProperty


class GlueAuthConfiguration(BaseModel):
    AuthenticationType: GlueProperty | None = None
    SecretArn: GlueProperty | None = None
    OAuth2Properties: dict[StrictStr, GlueProperty] | None = None
    BasicAuthenticationProperties: dict[StrictStr, GlueProperty] | None = None
    CustomAuthenticationProperties: dict[StrictStr, GlueProperty] | None = None
