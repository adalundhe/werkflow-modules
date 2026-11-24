from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lake_formation_lf_tag_expression import LakeFormationLFTagExpression


class LakeFormationListLFTagExpressionsResponse(BaseModel):
    LFTagExpressions: list[LakeFormationLFTagExpression] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
