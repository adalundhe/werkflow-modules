from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSPartialMatch(BaseModel):
    Reference: StrictStr | None = None
    TargetViolationReasons: list[StrictStr] | None = None
