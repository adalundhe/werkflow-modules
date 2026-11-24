from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .cloud_search_domain_endpoint_options_status import CloudSearchDomainEndpointOptionsStatus


class CloudSearchDescribeDomainEndpointOptionsResponse(BaseModel):
    DomainEndpointOptions: CloudSearchDomainEndpointOptionsStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
