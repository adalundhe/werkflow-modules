from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .connect_routing_profile_summary import ConnectRoutingProfileSummary


class ConnectListRoutingProfilesResponse(BaseModel):
    RoutingProfileSummaryList: list[ConnectRoutingProfileSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
