from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraStopDataSourceSyncJobRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
