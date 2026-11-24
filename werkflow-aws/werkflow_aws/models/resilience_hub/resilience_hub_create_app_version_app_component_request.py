from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubCreateAppVersionAppComponentRequest(BaseModel):
    appArn: StrictStr
    name: StrictStr
    type: StrictStr
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
    clientToken: StrictStr | None = None
    id: StrictStr | None = None
