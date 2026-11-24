from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_image_source import QuickSightImageSource


class QuickSightImageConfiguration(BaseModel):
    Source: QuickSightImageSource | None = None
