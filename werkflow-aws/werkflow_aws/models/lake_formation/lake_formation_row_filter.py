from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lake_formation_all_rows_wildcard import LakeFormationAllRowsWildcard


class LakeFormationRowFilter(BaseModel):
    FilterExpression: StrictStr | None = None
    AllRowsWildcard: LakeFormationAllRowsWildcard | None = None
