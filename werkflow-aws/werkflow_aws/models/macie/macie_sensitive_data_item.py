from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_default_detection import MacieDefaultDetection


class MacieSensitiveDataItem(BaseModel):
    category: StrictStr | None = None
    detections: list[MacieDefaultDetection] | None = None
    totalCount: StrictInt | None = None
