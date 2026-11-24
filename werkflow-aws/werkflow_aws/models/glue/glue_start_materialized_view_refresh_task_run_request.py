from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class GlueStartMaterializedViewRefreshTaskRunRequest(BaseModel):
    CatalogId: StrictStr
    DatabaseName: StrictStr
    TableName: StrictStr
    FullRefresh: StrictBool | None = None
