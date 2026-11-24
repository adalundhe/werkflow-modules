from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_column_hierarchy import QuickSightColumnHierarchy
from .quick_sight_visual_custom_action import QuickSightVisualCustomAction
from .quick_sight_visual_subtitle_label_options import QuickSightVisualSubtitleLabelOptions
from .quick_sight_visual_title_label_options import QuickSightVisualTitleLabelOptions
from .quick_sight_waterfall_chart_configuration import QuickSightWaterfallChartConfiguration


class QuickSightWaterfallVisual(BaseModel):
    VisualId: StrictStr | None = None
    Title: QuickSightVisualTitleLabelOptions | None = None
    Subtitle: QuickSightVisualSubtitleLabelOptions | None = None
    ChartConfiguration: QuickSightWaterfallChartConfiguration | None = None
    Actions: list[QuickSightVisualCustomAction] | None = None
    ColumnHierarchies: list[QuickSightColumnHierarchy] | None = None
    VisualContentAltText: StrictStr | None = None
