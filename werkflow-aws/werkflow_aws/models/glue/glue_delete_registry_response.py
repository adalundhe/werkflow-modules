from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueDeleteRegistryResponse(BaseModel):
    RegistryName: StrictStr | None = None
    RegistryArn: StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
