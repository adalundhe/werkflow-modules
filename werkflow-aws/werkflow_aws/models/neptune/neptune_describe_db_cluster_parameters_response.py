from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_parameter import NeptuneParameter


class NeptuneDescribeDBClusterParametersResponse(BaseModel):
    Parameters: list[NeptuneParameter] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
