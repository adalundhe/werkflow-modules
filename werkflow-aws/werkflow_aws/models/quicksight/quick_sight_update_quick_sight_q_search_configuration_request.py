from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateQuickSightQSearchConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
    QSearchStatus: Literal['ENABLED', 'DISABLED']
