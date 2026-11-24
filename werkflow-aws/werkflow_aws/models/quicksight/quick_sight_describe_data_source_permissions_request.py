from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDataSourcePermissionsRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSourceId: StrictStr
