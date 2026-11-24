from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_label_type import QuickSightDataLabelType
from .quick_sight_font_configuration import QuickSightFontConfiguration


class QuickSightDataLabelOptions(BaseModel):
    Visibility: StrictStr | None = None
    CategoryLabelVisibility: StrictStr | None = None
    MeasureLabelVisibility: StrictStr | None = None
    DataLabelTypes: list[QuickSightDataLabelType] | None = None
    Position: StrictStr | None = None
    LabelContent: StrictStr | None = None
    LabelFontConfiguration: QuickSightFontConfiguration | None = None
    LabelColor: StrictStr | None = None
    Overlap: StrictStr | None = None
    TotalsVisibility: StrictStr | None = None
