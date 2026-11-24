from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_route_server_bfd_status import EC2RouteServerBfdStatus
from .ec2_route_server_bgp_options import EC2RouteServerBgpOptions
from .ec2_route_server_bgp_status import EC2RouteServerBgpStatus
from .ec2_tag_model import EC2TagModel


class EC2RouteServerPeer(BaseModel):
    RouteServerPeerId: StrictStr | None = None
    RouteServerEndpointId: StrictStr | None = None
    RouteServerId: StrictStr | None = None
    VpcId: StrictStr | None = None
    SubnetId: StrictStr | None = None
    State: StrictStr | None = None
    FailureReason: StrictStr | None = None
    EndpointEniId: StrictStr | None = None
    EndpointEniAddress: StrictStr | None = None
    PeerAddress: StrictStr | None = None
    BgpOptions: EC2RouteServerBgpOptions | None = None
    BgpStatus: EC2RouteServerBgpStatus | None = None
    BfdStatus: EC2RouteServerBfdStatus | None = None
    Tags: list[EC2TagModel] | None = None
