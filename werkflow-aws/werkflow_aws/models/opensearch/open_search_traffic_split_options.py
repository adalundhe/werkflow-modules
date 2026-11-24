from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_traffic_percents import OpenSearchTrafficPercents


class OpenSearchTrafficSplitOptions(BaseModel):
    Current: OpenSearchTrafficPercents | None = None
    Target: OpenSearchTrafficPercents | None = None
    Status: StrictStr | None = None
