from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WorkSpacesWorkspaceConnectionStatus(BaseModel):
    WorkspaceId: StrictStr | None = None
    ConnectionState: StrictStr | None = None
    ConnectionStateCheckTimestamp: datetime.datetime | StrictStr | None = None
    LastKnownUserConnectionTimestamp: datetime.datetime | StrictStr | None = None
