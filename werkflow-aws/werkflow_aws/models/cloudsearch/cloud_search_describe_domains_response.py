from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_domain_status import CloudSearchDomainStatus


class CloudSearchDescribeDomainsResponse(BaseModel):
    DomainStatusList: list[CloudSearchDomainStatus] | None = None
    ResponseMetadata: dict[str, Any] | None = None
