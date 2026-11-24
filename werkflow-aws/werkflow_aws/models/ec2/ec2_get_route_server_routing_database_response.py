from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_route_server_route import EC2RouteServerRoute


class EC2GetRouteServerRoutingDatabaseResponse(BaseModel):
    AreRoutesPersisted: StrictBool | None = None
    Routes: list[EC2RouteServerRoute] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
