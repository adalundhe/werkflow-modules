from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateRoleAliasResponse(BaseModel):
    roleAlias: StrictStr | None = None
    roleAliasArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
