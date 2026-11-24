from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_mapped_data_set_parameter import QuickSightMappedDataSetParameter
from .quick_sight_string_default_values import QuickSightStringDefaultValues
from .quick_sight_string_value_when_unset_configuration import QuickSightStringValueWhenUnsetConfiguration


class QuickSightStringParameterDeclaration(BaseModel):
    ParameterValueType: StrictStr | None = None
    Name: StrictStr | None = None
    DefaultValues: QuickSightStringDefaultValues | None = None
    ValueWhenUnset: QuickSightStringValueWhenUnsetConfiguration | None = None
    MappedDataSetParameters: list[QuickSightMappedDataSetParameter] | None = None
