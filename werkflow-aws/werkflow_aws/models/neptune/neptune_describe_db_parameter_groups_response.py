from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_parameter_group import NeptuneDBParameterGroup


class NeptuneDescribeDBParameterGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBParameterGroups: list[NeptuneDBParameterGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
