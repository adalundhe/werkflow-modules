from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_partition_index_descriptor import GluePartitionIndexDescriptor


class GlueGetPartitionIndexesResponse(BaseModel):
    PartitionIndexDescriptorList: list[GluePartitionIndexDescriptor] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
