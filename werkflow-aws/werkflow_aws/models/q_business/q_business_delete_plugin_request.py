from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeletePluginRequest(BaseModel):
    applicationId: StrictStr
    pluginId: StrictStr
