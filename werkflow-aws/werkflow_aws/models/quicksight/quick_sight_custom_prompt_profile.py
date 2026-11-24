from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCustomPromptProfile(BaseModel):
    ModelProfileId: StrictStr
    SubscriptionId: StrictStr
    QbsAwsAccountId: StrictStr
