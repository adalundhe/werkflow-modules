from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class KendraCorrection(BaseModel):
    BeginOffset: StrictInt | None = None
    EndOffset: StrictInt | None = None
    Term: StrictStr | None = None
    CorrectedTerm: StrictStr | None = None
