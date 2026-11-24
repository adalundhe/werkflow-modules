from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeTemplateAliasRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    AliasName: StrictStr
