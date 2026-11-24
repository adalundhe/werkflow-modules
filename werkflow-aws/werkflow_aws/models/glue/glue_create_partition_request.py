from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_partition_input import GluePartitionInput


class GlueCreatePartitionRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    PartitionInput: GluePartitionInput
    CatalogId: StrictStr | None = None
