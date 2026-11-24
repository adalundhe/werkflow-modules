from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightDateAxisOptions(BaseModel):
    MissingDateVisibility: StrictStr | None = None
