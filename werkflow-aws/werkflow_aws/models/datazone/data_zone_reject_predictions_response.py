from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DataZoneRejectPredictionsResponse(BaseModel):
    domainId: StrictStr | None = None
    assetId: StrictStr | None = None
    assetRevision: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
