from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class ConnectDeleteContactDataResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
