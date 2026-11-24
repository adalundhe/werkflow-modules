from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetColumnStatisticsForTableRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    ColumnNames: list[StrictStr]
    CatalogId: StrictStr | None = None
