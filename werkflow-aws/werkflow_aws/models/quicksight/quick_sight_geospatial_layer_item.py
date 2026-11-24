from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_geospatial_data_source_item import QuickSightGeospatialDataSourceItem
from .quick_sight_geospatial_layer_definition import QuickSightGeospatialLayerDefinition
from .quick_sight_geospatial_layer_join_definition import QuickSightGeospatialLayerJoinDefinition
from .quick_sight_layer_custom_action import QuickSightLayerCustomAction
from .quick_sight_tooltip_options import QuickSightTooltipOptions


class QuickSightGeospatialLayerItem(BaseModel):
    LayerId: StrictStr | None = None
    LayerType: StrictStr | None = None
    DataSource: QuickSightGeospatialDataSourceItem | None = None
    Label: StrictStr | None = None
    Visibility: StrictStr | None = None
    LayerDefinition: QuickSightGeospatialLayerDefinition | None = None
    Tooltip: QuickSightTooltipOptions | None = None
    JoinDefinition: QuickSightGeospatialLayerJoinDefinition | None = None
    Actions: list[QuickSightLayerCustomAction] | None = None
