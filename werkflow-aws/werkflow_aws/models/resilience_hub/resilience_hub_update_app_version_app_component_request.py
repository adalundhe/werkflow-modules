from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubUpdateAppVersionAppComponentRequest(BaseModel):
    appArn: StrictStr
    id: StrictStr
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
