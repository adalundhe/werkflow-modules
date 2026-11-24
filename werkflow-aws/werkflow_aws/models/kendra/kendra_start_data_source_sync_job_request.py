from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraStartDataSourceSyncJobRequest(BaseModel):
    Id: StrictStr
    IndexId: StrictStr
