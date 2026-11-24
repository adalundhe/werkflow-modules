from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_orderable_db_instance_option import RDSOrderableDBInstanceOption


class RDSDescribeOrderableDBInstanceOptionsResponse(BaseModel):
    OrderableDBInstanceOptions: list[RDSOrderableDBInstanceOption] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
