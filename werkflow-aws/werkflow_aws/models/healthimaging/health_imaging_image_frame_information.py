from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingImageFrameInformation(BaseModel):
    imageFrameId: StrictStr
