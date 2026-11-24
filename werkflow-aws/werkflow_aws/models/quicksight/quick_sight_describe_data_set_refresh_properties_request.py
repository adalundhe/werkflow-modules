from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDataSetRefreshPropertiesRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
