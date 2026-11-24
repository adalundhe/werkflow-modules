from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightDynamicDefaultValue(BaseModel):
    UserNameColumn: QuickSightColumnIdentifier | None = None
    GroupNameColumn: QuickSightColumnIdentifier | None = None
    DefaultValueColumn: QuickSightColumnIdentifier | None = None
