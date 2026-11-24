from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightCreateTemplateAliasRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    AliasName: StrictStr
    TemplateVersionNumber: StrictInt
