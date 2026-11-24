from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSServiceConnectAccessLogConfiguration(BaseModel):
    format: StrictStr | None = None
    includeQueryParameters: StrictStr | None = None
