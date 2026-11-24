from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubAppComponent(BaseModel):
    additionalInfo: dict[StrictStr, list[StrictStr]] | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    type: StrictStr | None = None
