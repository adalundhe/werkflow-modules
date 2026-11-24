from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDeleteDataSetRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
