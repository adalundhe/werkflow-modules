from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class RedshiftModifyClusterParameterGroupResponse(BaseModel):
    ParameterGroupName: StrictStr | None = None
    ParameterGroupStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
