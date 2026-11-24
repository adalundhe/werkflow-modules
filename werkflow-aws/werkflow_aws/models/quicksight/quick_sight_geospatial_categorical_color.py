from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .quick_sight_geospatial_categorical_data_color import QuickSightGeospatialCategoricalDataColor
from .quick_sight_geospatial_null_data_settings import QuickSightGeospatialNullDataSettings


class QuickSightGeospatialCategoricalColor(BaseModel):
    CategoryDataColors: list[QuickSightGeospatialCategoricalDataColor] | None = None
    NullDataVisibility: StrictStr | None = None
    NullDataSettings: QuickSightGeospatialNullDataSettings | None = None
    DefaultOpacity: StrictFloat | StrictInt | None = None
