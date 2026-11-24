from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeQuickSightQSearchConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
