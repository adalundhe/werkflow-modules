from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeDataSourceRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSourceId: StrictStr
