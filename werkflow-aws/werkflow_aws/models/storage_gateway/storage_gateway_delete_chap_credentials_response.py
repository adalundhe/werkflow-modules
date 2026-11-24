from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteChapCredentialsResponse(BaseModel):
    TargetARN: StrictStr | None = None
    InitiatorName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
