from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeDatasetGroupRequest(BaseModel):
    datasetGroupArn: StrictStr
