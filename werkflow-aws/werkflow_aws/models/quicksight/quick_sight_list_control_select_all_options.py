from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightListControlSelectAllOptions(BaseModel):
    Visibility: StrictStr | None = None
