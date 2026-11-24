from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_axis_display_options import QuickSightAxisDisplayOptions
from .quick_sight_missing_data_configuration import QuickSightMissingDataConfiguration


class QuickSightLineSeriesAxisDisplayOptions(BaseModel):
    AxisOptions: QuickSightAxisDisplayOptions | None = None
    MissingDataConfigurations: list[QuickSightMissingDataConfiguration] | None = None
