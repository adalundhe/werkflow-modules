from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rdsdb_security_group import RDSDBSecurityGroup


class RDSDescribeDBSecurityGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBSecurityGroups: list[RDSDBSecurityGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
