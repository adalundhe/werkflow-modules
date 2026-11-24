from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QBusinessPlugin(BaseModel):
    pluginId: StrictStr | None = None
    displayName: StrictStr | None = None
    type: StrictStr | None = None
    serverUrl: StrictStr | None = None
    state: StrictStr | None = None
    buildStatus: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
