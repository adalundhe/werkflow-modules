from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_unfiltered_partition import GlueUnfilteredPartition


class GlueGetUnfilteredPartitionsMetadataResponse(BaseModel):
    UnfilteredPartitions: list[GlueUnfilteredPartition] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
