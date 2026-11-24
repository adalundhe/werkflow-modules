from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_session import GlueSession


class GlueGetSessionResponse(BaseModel):
    Session: GlueSession | None = None
    ResponseMetadata: dict[str, Any] | None = None
