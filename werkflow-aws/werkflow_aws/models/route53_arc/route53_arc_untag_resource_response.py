from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class Route53ARCUntagResourceResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
