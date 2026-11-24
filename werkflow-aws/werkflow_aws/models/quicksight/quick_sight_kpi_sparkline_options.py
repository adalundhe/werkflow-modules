from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightKPISparklineOptions(BaseModel):
    Visibility: StrictStr | None = None
    Type: StrictStr | None = None
    Color: StrictStr | None = None
    TooltipVisibility: StrictStr | None = None
