from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_routing_profile import ConnectRoutingProfile


class ConnectSearchRoutingProfilesResponse(BaseModel):
    RoutingProfiles: list[ConnectRoutingProfile] | None = None
    NextToken: StrictStr | None = None
    ApproximateTotalCount: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
