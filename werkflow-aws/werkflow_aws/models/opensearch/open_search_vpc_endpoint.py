from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_vpc_derived_info import OpenSearchVPCDerivedInfo


class OpenSearchVpcEndpoint(BaseModel):
    VpcEndpointId: StrictStr | None = None
    VpcEndpointOwner: StrictStr | None = None
    DomainArn: StrictStr | None = None
    VpcOptions: OpenSearchVPCDerivedInfo | None = None
    Status: StrictStr | None = None
    Endpoint: StrictStr | None = None
