from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDataQualityTargetTable(BaseModel):
    TableName: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    CatalogId: StrictStr | None = None
