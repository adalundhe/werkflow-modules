from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneAcceptPredictionsResponse(BaseModel):
    domainId: StrictStr | None = None
    assetId: StrictStr | None = None
    revision: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
