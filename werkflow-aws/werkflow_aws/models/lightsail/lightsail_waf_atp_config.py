from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_waf_response_inspection import LightsailWafResponseInspection


class LightsailWafAtpConfig(BaseModel):
    loginPath: StrictStr | None = None
    payloadType: StrictStr | None = None
    usernameField: StrictStr | None = None
    passwordField: StrictStr | None = None
    responseInspection: LightsailWafResponseInspection | None = None
