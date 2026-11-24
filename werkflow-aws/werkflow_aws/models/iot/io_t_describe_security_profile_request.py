from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeSecurityProfileRequest(BaseModel):
    securityProfileName: StrictStr
