from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAttachSecurityProfileRequest(BaseModel):
    securityProfileName: StrictStr
    securityProfileTargetArn: StrictStr
