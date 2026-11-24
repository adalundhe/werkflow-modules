from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteTemplateRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    VersionNumber: StrictInt | None = None
