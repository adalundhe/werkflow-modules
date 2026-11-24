from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDescribeTemplateRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    VersionNumber: StrictInt | None = None
    AliasName: StrictStr | None = None
