from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetDataSourceRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    dataSourceId: StrictStr
