from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_string_format_configuration import QuickSightStringFormatConfiguration


class QuickSightCategoricalDimensionField(BaseModel):
    FieldId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    HierarchyId: StrictStr | None = None
    FormatConfiguration: QuickSightStringFormatConfiguration | None = None
