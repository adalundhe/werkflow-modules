from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_image_source import QuickSightImageSource


class QuickSightImage(BaseModel):
    Source: QuickSightImageSource | None = None
    GeneratedImageUrl: StrictStr | None = None
