from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_dimension_field import QuickSightDimensionField
from .quick_sight_line_chart_marker_style_settings import QuickSightLineChartMarkerStyleSettings


class QuickSightSparklinesOptions(BaseModel):
    FieldId: StrictStr | None = None
    XAxisField: QuickSightDimensionField | None = None
    YAxisBehavior: StrictStr | None = None
    VisualType: StrictStr | None = None
    LineColor: StrictStr | None = None
    LineInterpolation: StrictStr | None = None
    AllPointsMarker: QuickSightLineChartMarkerStyleSettings | None = None
    MaxValueMarker: QuickSightLineChartMarkerStyleSettings | None = None
    MinValueMarker: QuickSightLineChartMarkerStyleSettings | None = None
