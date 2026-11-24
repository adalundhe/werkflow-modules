from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_path_value import QuickSightDataPathValue


class QuickSightDataPathColor(BaseModel):
    Element: QuickSightDataPathValue | None = None
    Color: StrictStr | None = None
    TimeGranularity: StrictStr | None = None
