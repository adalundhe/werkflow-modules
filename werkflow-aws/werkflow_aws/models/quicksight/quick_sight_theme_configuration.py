from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_data_color_palette import QuickSightDataColorPalette
from .quick_sight_sheet_style import QuickSightSheetStyle
from .quick_sight_typography import QuickSightTypography
from .quick_sight_ui_color_palette import QuickSightUIColorPalette


class QuickSightThemeConfiguration(BaseModel):
    DataColorPalette: QuickSightDataColorPalette | None = None
    UIColorPalette: QuickSightUIColorPalette | None = None
    Sheet: QuickSightSheetStyle | None = None
    Typography: QuickSightTypography | None = None
