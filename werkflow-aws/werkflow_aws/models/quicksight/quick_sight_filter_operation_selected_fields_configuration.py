from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier


class QuickSightFilterOperationSelectedFieldsConfiguration(BaseModel):
    SelectedFields: list[StrictStr] | None = None
    SelectedFieldOptions: StrictStr | None = None
    SelectedColumns: list[QuickSightColumnIdentifier] | None = None
