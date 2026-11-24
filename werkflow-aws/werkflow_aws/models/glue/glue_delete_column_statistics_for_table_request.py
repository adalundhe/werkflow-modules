from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteColumnStatisticsForTableRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    ColumnName: StrictStr
    CatalogId: StrictStr | None = None
