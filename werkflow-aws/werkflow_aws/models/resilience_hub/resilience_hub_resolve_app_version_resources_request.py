from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubResolveAppVersionResourcesRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
