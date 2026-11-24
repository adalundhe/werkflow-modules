from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_font_configuration import QuickSightFontConfiguration
from .quick_sight_global_table_border_options import QuickSightGlobalTableBorderOptions


class QuickSightTableCellStyle(BaseModel):
    Visibility: StrictStr | None = None
    FontConfiguration: QuickSightFontConfiguration | None = None
    TextWrap: StrictStr | None = None
    HorizontalTextAlignment: StrictStr | None = None
    VerticalTextAlignment: StrictStr | None = None
    BackgroundColor: StrictStr | None = None
    Height: StrictInt | None = None
    Border: QuickSightGlobalTableBorderOptions | None = None
