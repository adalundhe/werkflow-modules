from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_geospatial_layer_map_configuration import QuickSightGeospatialLayerMapConfiguration
from .quick_sight_visual_subtitle_label_options import QuickSightVisualSubtitleLabelOptions
from .quick_sight_visual_title_label_options import QuickSightVisualTitleLabelOptions


class QuickSightLayerMapVisual(BaseModel):
    VisualId: StrictStr | None = None
    Title: QuickSightVisualTitleLabelOptions | None = None
    Subtitle: QuickSightVisualSubtitleLabelOptions | None = None
    ChartConfiguration: QuickSightGeospatialLayerMapConfiguration | None = None
    DataSetIdentifier: StrictStr | None = None
    TopicIdentifier: StrictStr | None = None
    VisualContentAltText: StrictStr | None = None
