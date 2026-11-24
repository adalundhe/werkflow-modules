from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightDescribeAutomationJobRequest(BaseModel):
    AwsAccountId: StrictStr
    AutomationGroupId: StrictStr
    AutomationId: StrictStr
    JobId: StrictStr
    IncludeInputPayload: StrictBool | None = None
    IncludeOutputPayload: StrictBool | None = None
