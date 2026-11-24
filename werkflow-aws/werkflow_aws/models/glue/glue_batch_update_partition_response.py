from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_batch_update_partition_failure_entry import GlueBatchUpdatePartitionFailureEntry


class GlueBatchUpdatePartitionResponse(BaseModel):
    Errors: list[GlueBatchUpdatePartitionFailureEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
