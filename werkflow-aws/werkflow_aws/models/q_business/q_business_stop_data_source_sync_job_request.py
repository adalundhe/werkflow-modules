from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessStopDataSourceSyncJobRequest(BaseModel):
    dataSourceId: StrictStr
    applicationId: StrictStr
    indexId: StrictStr
