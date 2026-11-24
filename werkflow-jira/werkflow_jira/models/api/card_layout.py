from __future__ import annotations
from pydantic import BaseModel, StrictBool


class CardLayout(BaseModel):
    showDaysInColumn: StrictBool | None = None
