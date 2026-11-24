from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSServiceConnectContainerConfiguration(BaseModel):
    logLevel: StrictStr | None = None
