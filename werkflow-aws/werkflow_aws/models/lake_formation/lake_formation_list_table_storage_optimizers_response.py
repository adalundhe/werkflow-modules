from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_storage_optimizer import LakeFormationStorageOptimizer


class LakeFormationListTableStorageOptimizersResponse(BaseModel):
    StorageOptimizerList: list[LakeFormationStorageOptimizer] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
