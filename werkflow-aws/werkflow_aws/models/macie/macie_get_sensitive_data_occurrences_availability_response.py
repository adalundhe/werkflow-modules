from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieGetSensitiveDataOccurrencesAvailabilityResponse(BaseModel):
    code: StrictStr | None = None
    reasons: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
