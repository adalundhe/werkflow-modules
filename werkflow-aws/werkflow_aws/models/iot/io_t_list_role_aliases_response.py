from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTListRoleAliasesResponse(BaseModel):
    roleAliases: list[StrictStr] | None = None
    nextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
