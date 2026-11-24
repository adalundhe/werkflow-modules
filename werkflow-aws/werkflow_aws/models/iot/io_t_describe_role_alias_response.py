from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .io_t_role_alias_description import IoTRoleAliasDescription


class IoTDescribeRoleAliasResponse(BaseModel):
    roleAliasDescription: IoTRoleAliasDescription | None = None
    ResponseMetadata: dict[str, Any] | None = None
