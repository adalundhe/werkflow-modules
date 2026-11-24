from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class MigrationHubUpdateRouteResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    Arn: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    RouteId: StrictStr | None = None
    ServiceId: StrictStr | None = None
    State: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
