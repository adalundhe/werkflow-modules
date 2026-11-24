from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_parameter import RDSParameter


class RDSDescribeDBParametersResponse(BaseModel):
    Parameters: list[RDSParameter] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
