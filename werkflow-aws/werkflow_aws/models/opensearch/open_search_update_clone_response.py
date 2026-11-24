from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_cutover_options import OpenSearchCutoverOptions
from .open_search_retention_options import OpenSearchRetentionOptions
from .open_search_traffic_split_options import OpenSearchTrafficSplitOptions


class OpenSearchUpdateCloneResponse(BaseModel):
    DomainName: StrictStr | None = None
    ChangeId: StrictStr | None = None
    CutoverOptions: OpenSearchCutoverOptions | None = None
    TrafficSplitOptions: OpenSearchTrafficSplitOptions | None = None
    RetentionOptions: OpenSearchRetentionOptions | None = None
    ResponseMetadata: dict[str, Any] | None = None
