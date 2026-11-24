from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_inner_filter import QuickSightInnerFilter


class QuickSightNestedFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    IncludeInnerSet: StrictBool | None = None
    InnerFilter: QuickSightInnerFilter | None = None
