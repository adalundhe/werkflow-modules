from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDivergentField(BaseModel):
    Path: StrictStr | None = None
    SourceValue: StrictStr | None = None
    TargetValue: StrictStr | None = None
    Policy: StrictStr | None = None
