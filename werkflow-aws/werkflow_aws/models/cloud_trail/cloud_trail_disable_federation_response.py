from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudTrailDisableFederationResponse(BaseModel):
    EventDataStoreArn: StrictStr | None = None
    FederationStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
