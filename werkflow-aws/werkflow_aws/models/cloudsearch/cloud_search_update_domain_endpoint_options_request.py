from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .cloud_search_domain_endpoint_options import CloudSearchDomainEndpointOptions


class CloudSearchUpdateDomainEndpointOptionsRequest(BaseModel):
    DomainName: StrictStr
    DomainEndpointOptions: CloudSearchDomainEndpointOptions
