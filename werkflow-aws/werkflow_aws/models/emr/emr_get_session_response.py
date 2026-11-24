from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .emr_session import EMRSession


class EMRGetSessionResponse(BaseModel):
    Session: EMRSession | None = None
    ResponseMetadata: dict[str, Any] | None = None
