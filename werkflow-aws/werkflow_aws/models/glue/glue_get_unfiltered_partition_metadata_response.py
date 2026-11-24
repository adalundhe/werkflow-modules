from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_partition import GluePartition


class GlueGetUnfilteredPartitionMetadataResponse(BaseModel):
    Partition: GluePartition | None = None
    AuthorizedColumns: list[StrictStr] | None = None
    IsRegisteredWithLakeFormation: StrictBool | None = None
    ResponseMetadata: dict[str, Any] | None = None
