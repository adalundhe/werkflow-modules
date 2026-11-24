from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueGetRegistryResponse(BaseModel):
    RegistryName: StrictStr | None = None
    RegistryArn: StrictStr | None = None
    Description: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: StrictStr | None = None
    UpdatedTime: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
