from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class IoTListSecurityProfilesForTargetRequest(BaseModel):
    securityProfileTargetArn: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    recursive: StrictBool | None = None
