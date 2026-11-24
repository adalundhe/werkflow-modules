from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_virtual_object import LakeFormationVirtualObject


class LakeFormationDeleteObjectsOnCancelRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    TransactionId: StrictStr
    Objects: list[LakeFormationVirtualObject]
    CatalogId: StrictStr | None = None
