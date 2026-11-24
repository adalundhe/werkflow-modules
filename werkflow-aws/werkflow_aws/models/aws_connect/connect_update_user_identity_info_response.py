from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class ConnectUpdateUserIdentityInfoResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
