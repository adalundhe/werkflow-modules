from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieSeverityLevel(BaseModel):
    occurrencesThreshold: StrictInt | None = None
    severity: StrictStr | None = None
