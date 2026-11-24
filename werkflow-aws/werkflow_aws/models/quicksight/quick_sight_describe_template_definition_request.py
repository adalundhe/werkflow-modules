from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDescribeTemplateDefinitionRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
    VersionNumber: StrictInt | None = None
    AliasName: StrictStr | None = None
