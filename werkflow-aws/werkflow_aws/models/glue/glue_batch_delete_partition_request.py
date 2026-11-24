from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_partition_value_list import GluePartitionValueList


class GlueBatchDeletePartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionsToDelete: list[GluePartitionValueList]
    CatalogId: StrictStr | None = None
