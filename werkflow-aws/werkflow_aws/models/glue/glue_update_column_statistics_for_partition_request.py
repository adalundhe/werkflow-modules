from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_column_statistics import GlueColumnStatistics


class GlueUpdateColumnStatisticsForPartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionValues: list[StrictStr]
    ColumnStatisticsList: list[GlueColumnStatistics]
    CatalogId: StrictStr | None = None
