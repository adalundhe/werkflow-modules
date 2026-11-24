from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class TextractDeleteAdapterVersionResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
