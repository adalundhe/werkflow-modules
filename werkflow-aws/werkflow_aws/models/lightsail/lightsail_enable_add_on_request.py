from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lightsail_add_on_request import LightsailAddOnRequest


class LightsailEnableAddOnRequest(BaseModel):
    resourceName: StrictStr
    addOnRequest: LightsailAddOnRequest
