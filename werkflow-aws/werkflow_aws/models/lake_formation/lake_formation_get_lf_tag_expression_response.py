from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag import LakeFormationLFTag


class LakeFormationGetLFTagExpressionResponse(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CatalogId: StrictStr | None = None
    Expression: list[LakeFormationLFTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
