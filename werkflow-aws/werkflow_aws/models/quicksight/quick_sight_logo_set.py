from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_image_set import QuickSightImageSet


class QuickSightLogoSet(BaseModel):
    Primary: QuickSightImageSet | None = None
    Favicon: QuickSightImageSet | None = None
