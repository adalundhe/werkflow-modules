from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeDatasetRequest(BaseModel):
    datasetArn: StrictStr
