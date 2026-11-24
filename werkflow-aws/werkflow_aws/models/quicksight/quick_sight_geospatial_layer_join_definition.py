from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_geospatial_layer_color_field import QuickSightGeospatialLayerColorField
from .quick_sight_unaggregated_field import QuickSightUnaggregatedField


class QuickSightGeospatialLayerJoinDefinition(BaseModel):
    ShapeKeyField: StrictStr | None = None
    DatasetKeyField: QuickSightUnaggregatedField | None = None
    ColorField: QuickSightGeospatialLayerColorField | None = None
