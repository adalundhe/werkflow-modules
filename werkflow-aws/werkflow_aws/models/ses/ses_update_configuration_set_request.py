from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_message_security_options import SESMessageSecurityOptions


class SESUpdateConfigurationSetRequest(BaseModel):
    ConfigurationSetName: StrictStr
    MessageSecurityOptions: SESMessageSecurityOptions | None = None
