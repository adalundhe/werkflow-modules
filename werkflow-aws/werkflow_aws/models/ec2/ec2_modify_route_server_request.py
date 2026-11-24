from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyRouteServerRequest(BaseModel):
    RouteServerId: StrictStr
    PersistRoutes: Literal['enable', 'disable', 'reset'] | None = None
    PersistRoutesDuration: StrictInt | None = None
    SnsNotificationsEnabled: StrictBool | None = None
    DryRun: StrictBool | None = None
