from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag import LakeFormationLFTag


class LakeFormationLFTagPolicyResource(BaseModel):
    CatalogId: StrictStr | None = None
    ResourceType: StrictStr | None = None
    Expression: list[LakeFormationLFTag] | None = None
    ExpressionName: StrictStr | None = None
