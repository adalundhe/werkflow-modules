from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightCancelIngestionRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSetId: StrictStr
    IngestionId: StrictStr
