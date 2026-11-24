from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DirectConnectConfirmConnectionResponse(BaseModel):
    connectionState: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
