from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeAppVersionRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
