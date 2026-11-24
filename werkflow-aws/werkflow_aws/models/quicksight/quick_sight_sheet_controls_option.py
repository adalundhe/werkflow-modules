from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetControlsOption(BaseModel):
    VisibilityState: StrictStr | None = None
