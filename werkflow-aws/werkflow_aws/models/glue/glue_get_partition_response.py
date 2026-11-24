from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_partition import GluePartition


class GlueGetPartitionResponse(BaseModel):
    Partition: GluePartition | None = None
    ResponseMetadata: dict[str, Any] | None = None
