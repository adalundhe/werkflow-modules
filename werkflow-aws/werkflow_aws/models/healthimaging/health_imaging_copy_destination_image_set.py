from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingCopyDestinationImageSet(BaseModel):
    imageSetId: StrictStr
    latestVersionId: StrictStr
