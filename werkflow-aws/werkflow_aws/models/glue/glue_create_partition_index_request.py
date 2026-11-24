from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_partition_index import GluePartitionIndex


class GlueCreatePartitionIndexRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionIndex: GluePartitionIndex
    CatalogId: StrictStr | None = None
