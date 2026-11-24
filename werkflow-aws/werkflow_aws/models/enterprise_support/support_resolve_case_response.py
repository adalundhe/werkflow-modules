from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SupportResolveCaseResponse(BaseModel):
    initialCaseStatus: StrictStr | None = None
    finalCaseStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
