from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateSPICECapacityConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
    PurchaseMode: Literal['MANUAL', 'AUTO_PURCHASE']
