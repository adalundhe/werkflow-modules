from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetMaterializedViewRefreshTaskRunRequest(BaseModel):
    CatalogId: StrictStr
    MaterializedViewRefreshTaskRunId: StrictStr
