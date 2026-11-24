from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_cutover_request_options import OpenSearchCutoverRequestOptions
from .open_search_retention_options import OpenSearchRetentionOptions
from .open_search_traffic_split_request_options import OpenSearchTrafficSplitRequestOptions


class OpenSearchUpdateCloneRequest(BaseModel):
    DomainName: StrictStr
    TrafficSplitOptions: OpenSearchTrafficSplitRequestOptions | None = None
    CutoverOptions: OpenSearchCutoverRequestOptions | None = None
    RetentionOptions: OpenSearchRetentionOptions | None = None
