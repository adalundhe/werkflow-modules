from __future__ import annotations
from pydantic import BaseModel, StrictStr


class HealthImagingMetadataCopies(BaseModel):
    copiableAttributes: StrictStr
