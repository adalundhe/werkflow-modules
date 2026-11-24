from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteAccountSubscriptionRequest(BaseModel):
    AwsAccountId: StrictStr
