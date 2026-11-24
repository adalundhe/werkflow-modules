from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingDeleteImageSetRequest(BaseModel):
    datastoreId: StrictStr
    imageSetId: StrictStr
