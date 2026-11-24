from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_valid_db_instance_modifications_message import NeptuneValidDBInstanceModificationsMessage


class NeptuneDescribeValidDBInstanceModificationsResponse(BaseModel):
    ValidDBInstanceModificationsMessage: NeptuneValidDBInstanceModificationsMessage | None = None
    ResponseMetadata: dict[str, Any] | None = None
