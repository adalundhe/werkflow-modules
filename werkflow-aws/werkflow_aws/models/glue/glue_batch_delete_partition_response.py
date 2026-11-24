from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_partition_error import GluePartitionError


class GlueBatchDeletePartitionResponse(BaseModel):
    Errors: list[GluePartitionError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
