from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteColumnStatisticsForPartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionValues: list[StrictStr]
    ColumnName: StrictStr
    CatalogId: StrictStr | None = None
