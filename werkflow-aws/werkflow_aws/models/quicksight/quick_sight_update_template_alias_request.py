from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightUpdateTemplateAliasRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    AliasName: StrictStr
    TemplateVersionNumber: StrictInt
