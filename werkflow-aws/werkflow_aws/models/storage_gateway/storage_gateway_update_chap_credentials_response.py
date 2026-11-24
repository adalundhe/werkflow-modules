from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class StorageGatewayUpdateChapCredentialsResponse(BaseModel):
    TargetARN: StrictStr | None = None
    InitiatorName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
