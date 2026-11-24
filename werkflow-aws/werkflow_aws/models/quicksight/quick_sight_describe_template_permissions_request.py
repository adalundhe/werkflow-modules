from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeTemplatePermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    TemplateId: StrictStr
