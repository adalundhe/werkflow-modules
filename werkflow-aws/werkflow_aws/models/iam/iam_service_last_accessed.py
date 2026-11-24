from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .iam_tracked_action_last_accessed import IAMTrackedActionLastAccessed


class IAMServiceLastAccessed(BaseModel):
    ServiceName: StrictStr | None = None
    LastAuthenticated: datetime.datetime | StrictStr | None = None
    ServiceNamespace: StrictStr | None = None
    LastAuthenticatedEntity: StrictStr | None = None
    LastAuthenticatedRegion: StrictStr | None = None
    TotalAuthenticatedEntities: StrictInt | None = None
    TrackedActionsLastAccessed: list[IAMTrackedActionLastAccessed] | None = None
