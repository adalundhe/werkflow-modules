from __future__ import annotations
from pydantic import BaseModel
from .open_search_cluster_config import OpenSearchClusterConfig
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchClusterConfigStatus(BaseModel):
    Options: OpenSearchClusterConfig | None = None
    Status: OpenSearchOptionStatus | None = None
