from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteTemplateAliasRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    AliasName: StrictStr
