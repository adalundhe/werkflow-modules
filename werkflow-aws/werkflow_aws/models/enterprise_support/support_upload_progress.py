from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SupportUploadProgress(BaseModel):
    totalParts: StrictInt | None = None
    completedPartsCount: StrictInt | None = None
