from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_route_server_bgp_options_request import EC2RouteServerBgpOptionsRequest
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateRouteServerPeerRequest(BaseModel):
    RouteServerEndpointId: StrictStr
    PeerAddress: StrictStr
    BgpOptions: EC2RouteServerBgpOptionsRequest
    DryRun: StrictBool | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
