from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightMarginStyle(BaseModel):
    Show: StrictBool | None = None
