from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_security_group import RDSDBSecurityGroup


class RDSCreateDBSecurityGroupResponse(BaseModel):
    DBSecurityGroup: RDSDBSecurityGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
