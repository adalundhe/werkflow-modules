from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeAppVersionResourcesResolutionStatusRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
    resolutionId: StrictStr | None = None
