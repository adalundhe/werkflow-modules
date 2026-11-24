from __future__ import annotations
from pydantic import BaseModel
from .connect_preview import ConnectPreview


class ConnectAgentFirst(BaseModel):
    Preview: ConnectPreview | None = None
