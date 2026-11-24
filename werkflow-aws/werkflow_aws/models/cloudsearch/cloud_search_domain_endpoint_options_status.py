from __future__ import annotations
from pydantic import BaseModel
from .cloud_search_domain_endpoint_options import CloudSearchDomainEndpointOptions
from .cloud_search_option_status import CloudSearchOptionStatus


class CloudSearchDomainEndpointOptionsStatus(BaseModel):
    Options: CloudSearchDomainEndpointOptions | None = None
    Status: CloudSearchOptionStatus | None = None
