from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_valid_db_instance_modifications_message import RDSValidDBInstanceModificationsMessage


class RDSDescribeValidDBInstanceModificationsResponse(BaseModel):
    ValidDBInstanceModificationsMessage: RDSValidDBInstanceModificationsMessage | None = None
    ResponseMetadata: dict[str, Any] | None = None
