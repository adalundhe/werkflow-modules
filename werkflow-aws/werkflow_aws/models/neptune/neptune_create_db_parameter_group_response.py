from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_db_parameter_group import NeptuneDBParameterGroup


class NeptuneCreateDBParameterGroupResponse(BaseModel):
    DBParameterGroup: NeptuneDBParameterGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
