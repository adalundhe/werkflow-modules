from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationColumnWildcard(BaseModel):
    ExcludedColumnNames: list[StrictStr] | None = None
