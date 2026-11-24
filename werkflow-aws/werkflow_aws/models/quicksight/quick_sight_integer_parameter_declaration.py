from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_integer_default_values import QuickSightIntegerDefaultValues
from .quick_sight_integer_value_when_unset_configuration import QuickSightIntegerValueWhenUnsetConfiguration
from .quick_sight_mapped_data_set_parameter import QuickSightMappedDataSetParameter


class QuickSightIntegerParameterDeclaration(BaseModel):
    ParameterValueType: StrictStr | None = None
    Name: StrictStr | None = None
    DefaultValues: QuickSightIntegerDefaultValues | None = None
    ValueWhenUnset: QuickSightIntegerValueWhenUnsetConfiguration | None = None
    MappedDataSetParameters: list[QuickSightMappedDataSetParameter] | None = None
