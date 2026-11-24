from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_date_time_dataset_parameter_default_values import QuickSightDateTimeDatasetParameterDefaultValues


class QuickSightDateTimeDatasetParameter(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    ValueType: StrictStr | None = None
    TimeGranularity: StrictStr | None = None
    DefaultValues: QuickSightDateTimeDatasetParameterDefaultValues | None = None
