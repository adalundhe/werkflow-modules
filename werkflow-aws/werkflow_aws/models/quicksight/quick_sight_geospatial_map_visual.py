from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_hierarchy import QuickSightColumnHierarchy
from .quick_sight_geocode_preference import QuickSightGeocodePreference
from .quick_sight_geospatial_map_configuration import QuickSightGeospatialMapConfiguration
from .quick_sight_visual_custom_action import QuickSightVisualCustomAction
from .quick_sight_visual_subtitle_label_options import QuickSightVisualSubtitleLabelOptions
from .quick_sight_visual_title_label_options import QuickSightVisualTitleLabelOptions


class QuickSightGeospatialMapVisual(BaseModel):
    VisualId: StrictStr | None = None
    Title: QuickSightVisualTitleLabelOptions | None = None
    Subtitle: QuickSightVisualSubtitleLabelOptions | None = None
    ChartConfiguration: QuickSightGeospatialMapConfiguration | None = None
    ColumnHierarchies: list[QuickSightColumnHierarchy] | None = None
    Actions: list[QuickSightVisualCustomAction] | None = None
    VisualContentAltText: StrictStr | None = None
    GeocodingPreferences: list[QuickSightGeocodePreference] | None = None
