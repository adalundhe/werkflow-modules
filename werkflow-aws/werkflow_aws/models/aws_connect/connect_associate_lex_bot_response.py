from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class ConnectAssociateLexBotResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
