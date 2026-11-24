from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_description import QuickSightColumnDescription


class QuickSightColumnTag(BaseModel):
    ColumnGeographicRole: StrictStr | None = None
    ColumnDescription: QuickSightColumnDescription | None = None
