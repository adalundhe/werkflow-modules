from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ec2_route_server_association import EC2RouteServerAssociation


class EC2DisassociateRouteServerResponse(BaseModel):
    RouteServerAssociation: EC2RouteServerAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
