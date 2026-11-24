from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetColumnStatisticsForPartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionValues: list[StrictStr]
    ColumnNames: list[StrictStr]
    CatalogId: StrictStr | None = None
