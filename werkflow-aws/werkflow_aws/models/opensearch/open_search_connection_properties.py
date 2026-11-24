from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_cross_cluster_search_connection_properties import OpenSearchCrossClusterSearchConnectionProperties


class OpenSearchConnectionProperties(BaseModel):
    Endpoint: StrictStr | None = None
    CrossClusterSearch: OpenSearchCrossClusterSearchConnectionProperties | None = None
