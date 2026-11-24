from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_ipam_route_origin_authorization import EC2IpamRouteOriginAuthorization
from .ec2_ipam_route_overlap import EC2IpamRouteOverlap


class EC2IpamRouteProtectionFinding(BaseModel):
    ResourceOwnerId: StrictStr | None = None
    ResourceRegion: StrictStr | None = None
    IpamPoolId: StrictStr | None = None
    Cidr: StrictStr | None = None
    State: StrictStr | None = None
    AdvertisementType: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    PoolId: StrictStr | None = None
    Asn: StrictStr | None = None
    RpkiStatus: StrictStr | None = None
    RpkiStrength: StrictStr | None = None
    Roas: list[EC2IpamRouteOriginAuthorization] | None = None
    RouteOverlaps: list[EC2IpamRouteOverlap] | None = None
    SampleTime: datetime.datetime | StrictStr | None = None
    RoaSampleTime: datetime.datetime | StrictStr | None = None
