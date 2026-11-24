from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightStartAutomationJobRequest(BaseModel):
    AwsAccountId: StrictStr
    AutomationGroupId: StrictStr
    AutomationId: StrictStr
    InputPayload: StrictStr | None = None
