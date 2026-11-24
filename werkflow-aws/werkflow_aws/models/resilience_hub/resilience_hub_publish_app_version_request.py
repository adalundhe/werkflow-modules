from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubPublishAppVersionRequest(BaseModel):
    appArn: StrictStr
    versionName: StrictStr | None = None
