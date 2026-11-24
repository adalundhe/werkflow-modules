from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_layout_configuration import QuickSightLayoutConfiguration


class QuickSightLayout(BaseModel):
    Configuration: QuickSightLayoutConfiguration | None = None
