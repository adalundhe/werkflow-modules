from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUIColorPalette(BaseModel):
    PrimaryForeground: StrictStr | None = None
    PrimaryBackground: StrictStr | None = None
    SecondaryForeground: StrictStr | None = None
    SecondaryBackground: StrictStr | None = None
    Accent: StrictStr | None = None
    AccentForeground: StrictStr | None = None
    Danger: StrictStr | None = None
    DangerForeground: StrictStr | None = None
    Warning: StrictStr | None = None
    WarningForeground: StrictStr | None = None
    Success: StrictStr | None = None
    SuccessForeground: StrictStr | None = None
    Dimension: StrictStr | None = None
    DimensionForeground: StrictStr | None = None
    Measure: StrictStr | None = None
    MeasureForeground: StrictStr | None = None
