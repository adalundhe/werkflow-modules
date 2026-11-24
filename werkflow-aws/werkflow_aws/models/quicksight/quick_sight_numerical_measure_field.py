from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_number_format_configuration import QuickSightNumberFormatConfiguration
from .quick_sight_numerical_aggregation_function import QuickSightNumericalAggregationFunction


class QuickSightNumericalMeasureField(BaseModel):
    FieldId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    AggregationFunction: QuickSightNumericalAggregationFunction | None = None
    FormatConfiguration: QuickSightNumberFormatConfiguration | None = None
