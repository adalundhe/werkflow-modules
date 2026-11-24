from __future__ import annotations
from pydantic import BaseModel
from .lake_formation_batch_permissions_request_entry import LakeFormationBatchPermissionsRequestEntry
from .lake_formation_error_detail import LakeFormationErrorDetail


class LakeFormationBatchPermissionsFailureEntry(BaseModel):
    RequestEntry: LakeFormationBatchPermissionsRequestEntry | None = None
    Error: LakeFormationErrorDetail | None = None
