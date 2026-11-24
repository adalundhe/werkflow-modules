from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_occurrences import MacieOccurrences


class MacieDefaultDetection(BaseModel):
    count: StrictInt | None = None
    occurrences: MacieOccurrences | None = None
    type: StrictStr | None = None
