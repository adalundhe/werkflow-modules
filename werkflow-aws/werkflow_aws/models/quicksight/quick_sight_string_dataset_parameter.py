from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_string_dataset_parameter_default_values import QuickSightStringDatasetParameterDefaultValues


class QuickSightStringDatasetParameter(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    ValueType: StrictStr | None = None
    DefaultValues: QuickSightStringDatasetParameterDefaultValues | None = None
