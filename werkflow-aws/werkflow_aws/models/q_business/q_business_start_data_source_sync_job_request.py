from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessStartDataSourceSyncJobRequest(BaseModel):
    dataSourceId: StrictStr
    applicationId: StrictStr
    indexId: StrictStr
