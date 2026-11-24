from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .macie_occurrences import MacieOccurrences


class MacieCustomDetection(BaseModel):
    arn: StrictStr | None = None
    count: StrictInt | None = None
    name: StrictStr | None = None
    occurrences: MacieOccurrences | None = None
