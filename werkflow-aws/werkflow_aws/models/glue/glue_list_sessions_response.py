from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_session import GlueSession


class GlueListSessionsResponse(BaseModel):
    Ids: list[StrictStr] | None = None
    Sessions: list[GlueSession] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
