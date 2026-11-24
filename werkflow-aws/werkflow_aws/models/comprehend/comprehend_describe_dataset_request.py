from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeDatasetRequest(BaseModel):
    DatasetArn: StrictStr
