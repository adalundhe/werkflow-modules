from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightListControlSearchOptions(BaseModel):
    Visibility: StrictStr | None = None
