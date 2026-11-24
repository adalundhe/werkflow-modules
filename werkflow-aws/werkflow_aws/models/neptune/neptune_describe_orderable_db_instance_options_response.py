from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_orderable_db_instance_option import NeptuneOrderableDBInstanceOption


class NeptuneDescribeOrderableDBInstanceOptionsResponse(BaseModel):
    OrderableDBInstanceOptions: list[NeptuneOrderableDBInstanceOption] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
