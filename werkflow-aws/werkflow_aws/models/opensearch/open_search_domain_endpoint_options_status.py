from __future__ import annotations
from pydantic import BaseModel
from .open_search_domain_endpoint_options import OpenSearchDomainEndpointOptions
from .open_search_option_status import OpenSearchOptionStatus


class OpenSearchDomainEndpointOptionsStatus(BaseModel):
    Options: OpenSearchDomainEndpointOptions | None = None
    Status: OpenSearchOptionStatus | None = None
