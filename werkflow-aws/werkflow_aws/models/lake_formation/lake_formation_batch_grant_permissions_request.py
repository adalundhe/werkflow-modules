from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_batch_permissions_request_entry import LakeFormationBatchPermissionsRequestEntry


class LakeFormationBatchGrantPermissionsRequest(BaseModel):
    Entries: list[LakeFormationBatchPermissionsRequestEntry]
    CatalogId: StrictStr | None = None
