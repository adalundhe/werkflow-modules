from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_column import LakeFormationColumn


class LakeFormationRLSPolicy(BaseModel):
    CatalogId: StrictStr | None = None
    Name: StrictStr | None = None
    AttachmentColumns: list[LakeFormationColumn] | None = None
    FilterExpression: StrictStr | None = None
    Status: StrictStr | None = None
    StatusReason: StrictStr | None = None
