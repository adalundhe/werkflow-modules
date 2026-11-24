from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightAxisLabelReferenceOptions(BaseModel):
    FieldId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
