from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class MacieUpdateMacieSessionResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
