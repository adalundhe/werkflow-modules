from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDescribeDatasetRequest(BaseModel):
    DatasetArn: StrictStr
