from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class WAFv2DisassociateWebACLResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
