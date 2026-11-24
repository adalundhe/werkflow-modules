from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetPluginRequest(BaseModel):
    applicationId: StrictStr
    pluginId: StrictStr
