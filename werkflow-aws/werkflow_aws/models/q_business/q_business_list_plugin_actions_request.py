from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class QBusinessListPluginActionsRequest(BaseModel):
    applicationId: StrictStr
    pluginId: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
