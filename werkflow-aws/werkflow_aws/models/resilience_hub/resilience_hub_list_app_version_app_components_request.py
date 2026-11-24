from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubListAppVersionAppComponentsRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
