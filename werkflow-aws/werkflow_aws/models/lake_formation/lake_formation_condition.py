from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationCondition(BaseModel):
    Expression: StrictStr | None = None
