from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_tag import OpenSearchTag


class OpenSearchAddTagsRequest(BaseModel):
    ARN: StrictStr
    TagList: list[OpenSearchTag]
