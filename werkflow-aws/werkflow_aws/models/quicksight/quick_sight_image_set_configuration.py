from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_image_configuration import QuickSightImageConfiguration


class QuickSightImageSetConfiguration(BaseModel):
    Original: QuickSightImageConfiguration | None = None
