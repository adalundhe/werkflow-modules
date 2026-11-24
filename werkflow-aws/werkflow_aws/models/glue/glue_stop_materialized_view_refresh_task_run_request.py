from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueStopMaterializedViewRefreshTaskRunRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
