from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_decimal_dataset_parameter_default_values import QuickSightDecimalDatasetParameterDefaultValues


class QuickSightDecimalDatasetParameter(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    ValueType: StrictStr | None = None
    DefaultValues: QuickSightDecimalDatasetParameterDefaultValues | None = None
