from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeSelfUpgradeConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
