from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSServiceConnectServiceResource(BaseModel):
    discoveryName: StrictStr | None = None
    discoveryArn: StrictStr | None = None
