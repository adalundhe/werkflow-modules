from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ResilienceHubListMetricsResponse(BaseModel):
    nextToken: StrictStr | None = None
    rows: list[list[StrictStr]] | None = None
    ResponseMetadata: dict[str, Any] | None = None
