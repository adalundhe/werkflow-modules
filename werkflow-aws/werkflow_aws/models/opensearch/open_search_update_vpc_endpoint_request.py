from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_vpc_options import OpenSearchVPCOptions


class OpenSearchUpdateVpcEndpointRequest(BaseModel):
    VpcEndpointId: StrictStr
    VpcOptions: OpenSearchVPCOptions
