from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fis_action import FISAction


class FISGetActionResponse(BaseModel):
    action: FISAction | None = None
    ResponseMetadata: dict[str, Any] | None = None
