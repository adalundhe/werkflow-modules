from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_db_instance import NeptuneDBInstance


class NeptuneCreateDBInstanceResponse(BaseModel):
    DBInstance: NeptuneDBInstance | None = None
    ResponseMetadata: dict[str, Any] | None = None
