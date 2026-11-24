from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_search_result_item import GlueSearchResultItem


class GlueSearchAssetsResponse(BaseModel):
    Items: list[GlueSearchResultItem] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
