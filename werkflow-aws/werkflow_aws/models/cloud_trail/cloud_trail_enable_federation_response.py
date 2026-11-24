from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CloudTrailEnableFederationResponse(BaseModel):
    EventDataStoreArn: StrictStr | None = None
    FederationStatus: StrictStr | None = None
    FederationRoleArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
