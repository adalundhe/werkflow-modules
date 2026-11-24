from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class DataSyncDeleteTaskResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
