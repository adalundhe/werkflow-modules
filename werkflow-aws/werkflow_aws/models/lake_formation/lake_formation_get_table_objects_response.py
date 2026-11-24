from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_partition_objects import LakeFormationPartitionObjects


class LakeFormationGetTableObjectsResponse(BaseModel):
    Objects: list[LakeFormationPartitionObjects] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
