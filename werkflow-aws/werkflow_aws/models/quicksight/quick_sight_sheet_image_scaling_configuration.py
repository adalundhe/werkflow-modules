from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetImageScalingConfiguration(BaseModel):
    ScalingType: StrictStr | None = None
