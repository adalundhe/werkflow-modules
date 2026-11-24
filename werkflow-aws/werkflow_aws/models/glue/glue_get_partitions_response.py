from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_partition import GluePartition


class GlueGetPartitionsResponse(BaseModel):
    Partitions: list[GluePartition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
