from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteDataSourceRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSourceId: StrictStr
