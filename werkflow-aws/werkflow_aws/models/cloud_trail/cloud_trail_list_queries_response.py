from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_query import CloudTrailQuery


class CloudTrailListQueriesResponse(BaseModel):
    Queries: list[CloudTrailQuery] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
