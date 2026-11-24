from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteDataSetRefreshPropertiesRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
