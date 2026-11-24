from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueUpdateRegistryResponse(BaseModel):
    RegistryName: StrictStr | None = None
    RegistryArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
