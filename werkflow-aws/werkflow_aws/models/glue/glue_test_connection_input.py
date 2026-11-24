from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_authentication_configuration_input import GlueAuthenticationConfigurationInput


class GlueTestConnectionInput(BaseModel):
    ConnectionType: StrictStr
    ConnectionProperties: dict[StrictStr, StrictStr]
    AuthenticationConfiguration: GlueAuthenticationConfigurationInput | None = None
