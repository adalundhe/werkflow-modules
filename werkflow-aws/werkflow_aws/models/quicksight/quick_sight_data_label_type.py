from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_path_label_type import QuickSightDataPathLabelType
from .quick_sight_field_label_type import QuickSightFieldLabelType
from .quick_sight_maximum_label_type import QuickSightMaximumLabelType
from .quick_sight_minimum_label_type import QuickSightMinimumLabelType
from .quick_sight_range_ends_label_type import QuickSightRangeEndsLabelType


class QuickSightDataLabelType(BaseModel):
    FieldLabelType: QuickSightFieldLabelType | None = None
    DataPathLabelType: QuickSightDataPathLabelType | None = None
    RangeEndsLabelType: QuickSightRangeEndsLabelType | None = None
    MinimumLabelType: QuickSightMinimumLabelType | None = None
    MaximumLabelType: QuickSightMaximumLabelType | None = None
