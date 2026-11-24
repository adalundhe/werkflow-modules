from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteDatasetGroupRequest(BaseModel):
    datasetGroupArn: StrictStr
