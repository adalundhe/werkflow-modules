from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDescribeRoleAliasRequest(BaseModel):
    roleAlias: StrictStr
