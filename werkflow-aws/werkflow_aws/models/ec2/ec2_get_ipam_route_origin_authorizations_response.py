from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_ipam_route_origin_authorization_info import EC2IpamRouteOriginAuthorizationInfo


class EC2GetIpamRouteOriginAuthorizationsResponse(BaseModel):
    IpamRouteOriginAuthorizations: list[EC2IpamRouteOriginAuthorizationInfo] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
