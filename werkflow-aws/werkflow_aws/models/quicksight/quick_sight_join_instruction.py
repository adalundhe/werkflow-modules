from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_join_key_properties import QuickSightJoinKeyProperties


class QuickSightJoinInstruction(BaseModel):
    LeftOperand: StrictStr | None = None
    RightOperand: StrictStr | None = None
    LeftJoinKeyProperties: QuickSightJoinKeyProperties | None = None
    RightJoinKeyProperties: QuickSightJoinKeyProperties | None = None
    Type: StrictStr | None = None
    OnClause: StrictStr | None = None
