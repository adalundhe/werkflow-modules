from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_partition_input import GluePartitionInput


class GlueBatchUpdatePartitionRequestEntry(BaseModel):
    PartitionValueList: list[StrictStr]
    PartitionInput: GluePartitionInput
