from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_number_format_configuration import QuickSightNumberFormatConfiguration


class QuickSightNumericalDimensionField(BaseModel):
    FieldId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    HierarchyId: StrictStr | None = None
    FormatConfiguration: QuickSightNumberFormatConfiguration | None = None
