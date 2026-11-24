from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_brand_color_palette import QuickSightBrandColorPalette
from .quick_sight_brand_element_style import QuickSightBrandElementStyle
from .quick_sight_contextual_accent_palette import QuickSightContextualAccentPalette


class QuickSightApplicationTheme(BaseModel):
    BrandColorPalette: QuickSightBrandColorPalette | None = None
    ContextualAccentPalette: QuickSightContextualAccentPalette | None = None
    BrandElementStyle: QuickSightBrandElementStyle | None = None
