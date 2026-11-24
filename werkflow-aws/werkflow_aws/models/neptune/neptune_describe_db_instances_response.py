from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_db_instance import NeptuneDBInstance


class NeptuneDescribeDBInstancesResponse(BaseModel):
    Marker: StrictStr | None = None
    DBInstances: list[NeptuneDBInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
