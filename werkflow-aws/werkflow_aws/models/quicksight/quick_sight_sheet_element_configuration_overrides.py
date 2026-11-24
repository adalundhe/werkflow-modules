from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightSheetElementConfigurationOverrides(BaseModel):
    Visibility: StrictStr | None = None
