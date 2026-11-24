from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubDescribeAppVersionTemplateRequest(BaseModel):
    appArn: StrictStr
    appVersion: StrictStr
