from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_partition_input import GluePartitionInput


class GlueUpdatePartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionValueList: list[StrictStr]
    PartitionInput: GluePartitionInput
    CatalogId: StrictStr | None = None
