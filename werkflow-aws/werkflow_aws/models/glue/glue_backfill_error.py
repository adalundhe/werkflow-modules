from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_partition_value_list import GluePartitionValueList


class GlueBackfillError(BaseModel):
    Code: StrictStr | None = None
    Partitions: list[GluePartitionValueList] | None = None
