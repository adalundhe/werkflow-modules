from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class InputStreamSource(BaseModel):
    inputStream: dict[StrictStr, Any] | None = None
