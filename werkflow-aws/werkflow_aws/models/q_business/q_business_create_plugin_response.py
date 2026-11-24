from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class QBusinessCreatePluginResponse(BaseModel):
    pluginId: StrictStr | None = None
    pluginArn: StrictStr | None = None
    buildStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
