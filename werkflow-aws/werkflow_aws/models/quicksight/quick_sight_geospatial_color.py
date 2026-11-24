from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_geospatial_categorical_color import QuickSightGeospatialCategoricalColor
from .quick_sight_geospatial_gradient_color import QuickSightGeospatialGradientColor
from .quick_sight_geospatial_solid_color import QuickSightGeospatialSolidColor


class QuickSightGeospatialColor(BaseModel):
    Solid: QuickSightGeospatialSolidColor | None = None
    Gradient: QuickSightGeospatialGradientColor | None = None
    Categorical: QuickSightGeospatialCategoricalColor | None = None
