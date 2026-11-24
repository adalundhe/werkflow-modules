from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .migration_hub_default_route_input import MigrationHubDefaultRouteInput
from .migration_hub_uri_path_route_input import MigrationHubUriPathRouteInput


class MigrationHubCreateRouteRequest(BaseModel):
    ApplicationIdentifier: StrictStr
    EnvironmentIdentifier: StrictStr
    RouteType: Literal['DEFAULT', 'URI_PATH']
    ServiceIdentifier: StrictStr
    ClientToken: StrictStr | None = None
    DefaultRoute: MigrationHubDefaultRouteInput | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    UriPathRoute: MigrationHubUriPathRouteInput | None = None
