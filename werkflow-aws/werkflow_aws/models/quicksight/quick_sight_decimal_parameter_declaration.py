from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_decimal_default_values import QuickSightDecimalDefaultValues
from .quick_sight_decimal_value_when_unset_configuration import QuickSightDecimalValueWhenUnsetConfiguration
from .quick_sight_mapped_data_set_parameter import QuickSightMappedDataSetParameter


class QuickSightDecimalParameterDeclaration(BaseModel):
    ParameterValueType: StrictStr | None = None
    Name: StrictStr | None = None
    DefaultValues: QuickSightDecimalDefaultValues | None = None
    ValueWhenUnset: QuickSightDecimalValueWhenUnsetConfiguration | None = None
    MappedDataSetParameters: list[QuickSightMappedDataSetParameter] | None = None
