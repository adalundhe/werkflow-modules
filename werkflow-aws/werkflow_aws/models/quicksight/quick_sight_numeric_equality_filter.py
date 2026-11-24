from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .quick_sight_aggregation_function import QuickSightAggregationFunction
from .quick_sight_column_identifier import QuickSightColumnIdentifier
from .quick_sight_default_filter_control_configuration import QuickSightDefaultFilterControlConfiguration


class QuickSightNumericEqualityFilter(BaseModel):
    FilterId: StrictStr | None = None
    Column: QuickSightColumnIdentifier | None = None
    Value: StrictFloat | StrictInt | None = None
    SelectAllOptions: StrictStr | None = None
    MatchOperator: StrictStr | None = None
    AggregationFunction: QuickSightAggregationFunction | None = None
    ParameterName: StrictStr | None = None
    NullOption: StrictStr | None = None
    DefaultFilterControlConfiguration: QuickSightDefaultFilterControlConfiguration | None = None
