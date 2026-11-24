from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_tag import QuickSightColumnTag


class QuickSightTagColumnOperation(BaseModel):
    ColumnName: StrictStr | None = None
    Tags: list[QuickSightColumnTag] | None = None
