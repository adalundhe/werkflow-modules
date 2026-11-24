from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_detection import MacieDetection


class MacieListResourceProfileDetectionsResponse(BaseModel):
    detections: list[MacieDetection] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
