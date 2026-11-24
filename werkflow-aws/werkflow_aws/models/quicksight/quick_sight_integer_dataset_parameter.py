from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_integer_dataset_parameter_default_values import QuickSightIntegerDatasetParameterDefaultValues


class QuickSightIntegerDatasetParameter(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    ValueType: StrictStr | None = None
    DefaultValues: QuickSightIntegerDatasetParameterDefaultValues | None = None
