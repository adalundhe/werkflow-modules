from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_subnet_group import RDSDBSubnetGroup


class RDSDescribeDBSubnetGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBSubnetGroups: list[RDSDBSubnetGroup] | None = None
