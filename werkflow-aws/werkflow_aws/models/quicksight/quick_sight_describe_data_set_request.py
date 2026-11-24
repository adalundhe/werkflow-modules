from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDataSetRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
