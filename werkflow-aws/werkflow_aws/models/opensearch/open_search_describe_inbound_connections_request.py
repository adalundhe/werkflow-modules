from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .open_search_filter import OpenSearchFilter


class OpenSearchDescribeInboundConnectionsRequest(BaseModel):
    Filters: list[OpenSearchFilter] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
