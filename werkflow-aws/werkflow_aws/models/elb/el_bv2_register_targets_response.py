from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class ELBv2RegisterTargetsResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
