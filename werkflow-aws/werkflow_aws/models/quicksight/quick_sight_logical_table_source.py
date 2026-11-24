from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_join_instruction import QuickSightJoinInstruction


class QuickSightLogicalTableSource(BaseModel):
    JoinInstruction: QuickSightJoinInstruction | None = None
    PhysicalTableId: StrictStr | None = None
    DataSetArn: StrictStr | None = None
