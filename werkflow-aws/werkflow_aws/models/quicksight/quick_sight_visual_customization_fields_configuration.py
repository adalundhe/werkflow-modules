from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightVisualCustomizationFieldsConfiguration(BaseModel):
    Status: StrictStr | None = None
    AdditionalFields: list[QuickSightColumnIdentifier] | None = None
