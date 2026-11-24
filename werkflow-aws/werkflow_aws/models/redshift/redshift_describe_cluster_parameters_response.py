from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_parameter import RedshiftParameter


class RedshiftDescribeClusterParametersResponse(BaseModel):
    Parameters: list[RedshiftParameter] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
