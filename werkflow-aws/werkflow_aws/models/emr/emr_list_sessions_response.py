from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .emr_session import EMRSession


class EMRListSessionsResponse(BaseModel):
    Sessions: list[EMRSession] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
