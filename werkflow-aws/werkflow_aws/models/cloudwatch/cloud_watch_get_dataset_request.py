from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchGetDatasetRequest(BaseModel):
    DatasetIdentifier: StrictStr
