from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueCreateRegistryResponse(BaseModel):
    RegistryArn: StrictStr | None = None
    RegistryName: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
