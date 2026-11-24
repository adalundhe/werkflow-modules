from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_write_operation import LakeFormationWriteOperation


class LakeFormationUpdateTableObjectsRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    WriteOperations: list[LakeFormationWriteOperation]
    CatalogId: StrictStr | None = None
    TransactionId: StrictStr | None = None
