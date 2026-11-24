from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRuntimeToolReference(BaseModel):
    type: StrictStr | None = None
    name: StrictStr | None = None
    serverName: StrictStr | None = None
