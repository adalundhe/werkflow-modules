from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_parameter_group_model import RDSDBParameterGroupModel


class RDSCreateDBParameterGroupResponse(BaseModel):
    DBParameterGroup: RDSDBParameterGroupModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
