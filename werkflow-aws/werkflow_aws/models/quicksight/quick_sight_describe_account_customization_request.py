from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class QuickSightDescribeAccountCustomizationRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr | None = None
    Resolved: StrictBool | None = None
