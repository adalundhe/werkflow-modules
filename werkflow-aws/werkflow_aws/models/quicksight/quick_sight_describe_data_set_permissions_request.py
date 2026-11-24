from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDataSetPermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
