from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_identifier import QuickSightIdentifier


class QuickSightTopicSortClause(BaseModel):
    Operand: QuickSightIdentifier | None = None
    SortDirection: StrictStr | None = None
