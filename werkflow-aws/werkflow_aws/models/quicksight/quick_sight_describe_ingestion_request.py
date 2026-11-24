from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDescribeIngestionRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
    IngestionId: StrictStr
