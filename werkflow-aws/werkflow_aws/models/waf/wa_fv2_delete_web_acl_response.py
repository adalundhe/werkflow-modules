from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class WAFv2DeleteWebACLResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
