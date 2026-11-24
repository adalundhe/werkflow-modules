from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_session import GlueSession


class GlueCreateSessionResponse(BaseModel):
    Session: GlueSession | None = None
    ResponseMetadata: dict[str, Any] | None = None
