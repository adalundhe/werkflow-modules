from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectCreateRoutingProfileResponse(BaseModel):
    RoutingProfileArn: StrictStr | None = None
    RoutingProfileId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
