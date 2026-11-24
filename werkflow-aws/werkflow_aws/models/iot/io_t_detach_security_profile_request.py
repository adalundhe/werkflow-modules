from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDetachSecurityProfileRequest(BaseModel):
    securityProfileName: StrictStr
    securityProfileTargetArn: StrictStr
