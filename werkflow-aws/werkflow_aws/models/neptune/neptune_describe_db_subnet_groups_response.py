from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_subnet_group import NeptuneDBSubnetGroup


class NeptuneDescribeDBSubnetGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBSubnetGroups: list[NeptuneDBSubnetGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
