from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateSelfUpgradeConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
    Namespace: StrictStr
    SelfUpgradeStatus: Literal['AUTO_APPROVAL', 'ADMIN_APPROVAL']
