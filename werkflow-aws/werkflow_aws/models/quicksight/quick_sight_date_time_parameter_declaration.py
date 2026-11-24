from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_date_time_default_values import QuickSightDateTimeDefaultValues
from .quick_sight_date_time_value_when_unset_configuration import QuickSightDateTimeValueWhenUnsetConfiguration
from .quick_sight_mapped_data_set_parameter import QuickSightMappedDataSetParameter


class QuickSightDateTimeParameterDeclaration(BaseModel):
    Name: StrictStr | None = None
    DefaultValues: QuickSightDateTimeDefaultValues | None = None
    TimeGranularity: StrictStr | None = None
    ValueWhenUnset: QuickSightDateTimeValueWhenUnsetConfiguration | None = None
    MappedDataSetParameters: list[QuickSightMappedDataSetParameter] | None = None
