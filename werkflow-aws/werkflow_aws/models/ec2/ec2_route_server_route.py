from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_route_server_route_installation_detail import EC2RouteServerRouteInstallationDetail


class EC2RouteServerRoute(BaseModel):
    RouteServerEndpointId: StrictStr | None = None
    RouteServerPeerId: StrictStr | None = None
    RouteInstallationDetails: list[EC2RouteServerRouteInstallationDetail] | None = None
    RouteStatus: StrictStr | None = None
    Prefix: StrictStr | None = None
    AsPaths: list[StrictStr] | None = None
    Med: StrictInt | None = None
    NextHopIp: StrictStr | None = None
