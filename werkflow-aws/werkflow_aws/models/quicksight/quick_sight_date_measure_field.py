from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_date_time_format_configuration import QuickSightDateTimeFormatConfiguration


class QuickSightDateMeasureField(BaseModel):
    FieldId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    AggregationFunction: StrictStr | None = None
    FormatConfiguration: QuickSightDateTimeFormatConfiguration | None = None
