from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_partition import GluePartition
from .glue_partition_value_list import GluePartitionValueList


class GlueBatchGetPartitionResponse(BaseModel):
    Partitions: list[GluePartition] | None = None
    UnprocessedKeys: list[GluePartitionValueList] | None = None
    ResponseMetadata: dict[str, Any] | None = None
