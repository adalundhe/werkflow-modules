from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_partition_input import GluePartitionInput


class GlueBatchCreatePartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionInputList: list[GluePartitionInput]
    CatalogId: StrictStr | None = None
