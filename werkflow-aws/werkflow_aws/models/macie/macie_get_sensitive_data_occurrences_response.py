from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .macie_detected_data_details import MacieDetectedDataDetails


class MacieGetSensitiveDataOccurrencesResponse(BaseModel):
    error: StrictStr | None = None
    sensitiveDataOccurrences: dict[StrictStr, list[MacieDetectedDataDetails]] | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
