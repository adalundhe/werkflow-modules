from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightListRefreshSchedulesRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
