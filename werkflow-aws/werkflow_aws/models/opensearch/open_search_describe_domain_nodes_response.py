from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_domain_nodes_status import OpenSearchDomainNodesStatus


class OpenSearchDescribeDomainNodesResponse(BaseModel):
    DomainNodesStatusList: list[OpenSearchDomainNodesStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
