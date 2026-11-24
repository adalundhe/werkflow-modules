from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeQPersonalizationConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
