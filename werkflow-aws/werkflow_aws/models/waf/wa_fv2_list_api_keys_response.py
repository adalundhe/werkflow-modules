from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .wa_fv2_api_key_summary import WAFv2APIKeySummary


class WAFv2ListAPIKeysResponse(BaseModel):
    NextMarker: StrictStr | None = None
    APIKeySummaries: list[WAFv2APIKeySummary] | None = None
    ApplicationIntegrationURL: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
