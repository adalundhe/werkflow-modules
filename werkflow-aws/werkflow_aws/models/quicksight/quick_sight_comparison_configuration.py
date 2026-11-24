from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_comparison_format_configuration import QuickSightComparisonFormatConfiguration


class QuickSightComparisonConfiguration(BaseModel):
    ComparisonMethod: StrictStr | None = None
    ComparisonFormat: QuickSightComparisonFormatConfiguration | None = None
