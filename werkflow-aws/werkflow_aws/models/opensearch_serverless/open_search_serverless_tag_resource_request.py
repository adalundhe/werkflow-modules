from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_serverless_tag import OpenSearchServerlessTag


class OpenSearchServerlessTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[OpenSearchServerlessTag]
