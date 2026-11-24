from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeAppVersionAppComponentRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
    id: StrictStr
