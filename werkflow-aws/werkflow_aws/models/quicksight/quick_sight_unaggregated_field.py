from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_format_configuration import QuickSightFormatConfiguration


class QuickSightUnaggregatedField(BaseModel):
    FieldId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    FormatConfiguration: QuickSightFormatConfiguration | None = None
