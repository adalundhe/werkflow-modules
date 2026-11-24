from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class SESUpdateContactResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
