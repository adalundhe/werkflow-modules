from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .macie_custom_detection import MacieCustomDetection


class MacieCustomDataIdentifiers(BaseModel):
    detections: list[MacieCustomDetection] | None = None
    totalCount: StrictInt | None = None
