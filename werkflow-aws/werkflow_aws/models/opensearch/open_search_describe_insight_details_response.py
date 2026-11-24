from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_insight_field import OpenSearchInsightField


class OpenSearchDescribeInsightDetailsResponse(BaseModel):
    Fields: list[OpenSearchInsightField] | None = None
    ResponseMetadata: dict[str, Any] | None = None
