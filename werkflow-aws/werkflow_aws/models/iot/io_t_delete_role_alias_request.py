from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteRoleAliasRequest(BaseModel):
    roleAlias: StrictStr
