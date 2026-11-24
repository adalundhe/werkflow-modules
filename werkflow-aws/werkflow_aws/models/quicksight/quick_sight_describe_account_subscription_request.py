from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeAccountSubscriptionRequest(BaseModel):
    AwsAccountId: StrictStr
