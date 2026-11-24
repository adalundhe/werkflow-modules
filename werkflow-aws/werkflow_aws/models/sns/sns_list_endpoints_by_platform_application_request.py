from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSListEndpointsByPlatformApplicationRequest(BaseModel):
    PlatformApplicationArn: StrictStr
    NextToken: StrictStr | None = None
