from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_image_set_configuration import QuickSightImageSetConfiguration


class QuickSightLogoSetConfiguration(BaseModel):
    Primary: QuickSightImageSetConfiguration | None = None
    Favicon: QuickSightImageSetConfiguration | None = None
