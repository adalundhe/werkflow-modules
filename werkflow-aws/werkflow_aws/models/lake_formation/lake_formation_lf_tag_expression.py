from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag import LakeFormationLFTag


class LakeFormationLFTagExpression(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CatalogId: StrictStr | None = None
    Expression: list[LakeFormationLFTag] | None = None
