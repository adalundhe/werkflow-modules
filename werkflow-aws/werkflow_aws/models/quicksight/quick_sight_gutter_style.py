from __future__ import annotations
from pydantic import BaseModel, StrictBool


class QuickSightGutterStyle(BaseModel):
    Show: StrictBool | None = None
