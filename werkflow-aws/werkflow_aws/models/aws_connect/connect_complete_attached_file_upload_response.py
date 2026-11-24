from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class ConnectCompleteAttachedFileUploadResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
