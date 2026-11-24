from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ConnectStartEmailContactResponse(BaseModel):
    ContactId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
