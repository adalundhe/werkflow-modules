from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .migration_hub_uri_path_route_input import MigrationHubUriPathRouteInput


class MigrationHubCreateRouteResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    CreatedByAccountId: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    OwnerAccountId: StrictStr | None = None
    RouteId: StrictStr | None = None
    RouteType: StrictStr | None = None
    ServiceId: StrictStr | None = None
    State: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    UriPathRoute: MigrationHubUriPathRouteInput | None = None
    ResponseMetadata: dict[str, Any] | None = None
