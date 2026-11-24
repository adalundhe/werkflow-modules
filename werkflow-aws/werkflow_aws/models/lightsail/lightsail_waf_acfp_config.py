from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_waf_response_inspection import LightsailWafResponseInspection


class LightsailWafAcfpConfig(BaseModel):
    payloadType: StrictStr | None = None
    creationPath: StrictStr | None = None
    registrationPagePath: StrictStr | None = None
    responseInspection: LightsailWafResponseInspection | None = None
