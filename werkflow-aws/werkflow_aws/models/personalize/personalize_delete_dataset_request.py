from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDeleteDatasetRequest(BaseModel):
    datasetArn: StrictStr
