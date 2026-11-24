from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubUpdateAppVersionRequest(BaseModel):
    appArn: StrictStr
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
