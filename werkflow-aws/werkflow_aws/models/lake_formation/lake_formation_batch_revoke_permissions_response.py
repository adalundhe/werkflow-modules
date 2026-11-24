from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lake_formation_batch_permissions_failure_entry import LakeFormationBatchPermissionsFailureEntry


class LakeFormationBatchRevokePermissionsResponse(BaseModel):
    Failures: list[LakeFormationBatchPermissionsFailureEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
