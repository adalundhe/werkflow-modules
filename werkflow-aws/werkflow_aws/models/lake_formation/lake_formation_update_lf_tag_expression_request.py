from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag import LakeFormationLFTag


class LakeFormationUpdateLFTagExpressionRequest(BaseModel):
    Name: StrictStr
    Expression: list[LakeFormationLFTag]
    Description: StrictStr | None = None
    CatalogId: StrictStr | None = None
