from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueListCrawlersRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
