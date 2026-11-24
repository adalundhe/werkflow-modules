from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateDashboardsQAConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
    DashboardsQAStatus: Literal['ENABLED', 'DISABLED']
