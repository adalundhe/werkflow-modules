from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightKPIVisualStandardLayout(BaseModel):
    Type: StrictStr | None = None
