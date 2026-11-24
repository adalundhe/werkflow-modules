from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class ResilienceHubPublishAppVersionResponse(BaseModel):
    appArn: StrictStr | None = None
    appVersion: StrictStr | None = None
    identifier: StrictInt | None = None
    versionName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
