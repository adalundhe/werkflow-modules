from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .quick_sight_geospatial_gradient_step_color import QuickSightGeospatialGradientStepColor
from .quick_sight_geospatial_null_data_settings import QuickSightGeospatialNullDataSettings


class QuickSightGeospatialGradientColor(BaseModel):
    StepColors: list[QuickSightGeospatialGradientStepColor] | None = None
    NullDataVisibility: StrictStr | None = None
    NullDataSettings: QuickSightGeospatialNullDataSettings | None = None
    DefaultOpacity: StrictFloat | StrictInt | None = None
