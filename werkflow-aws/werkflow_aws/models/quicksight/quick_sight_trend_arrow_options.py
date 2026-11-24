from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTrendArrowOptions(BaseModel):
    Visibility: StrictStr | None = None
