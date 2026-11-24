from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_image import QuickSightImage


class QuickSightImageSet(BaseModel):
    Original: QuickSightImage | None = None
    Height64: QuickSightImage | None = None
    Height32: QuickSightImage | None = None
