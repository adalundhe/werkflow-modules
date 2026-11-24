from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rdsdb_instance_model import RDSDBInstanceModel


class RDSRestoreDBInstanceFromDBSnapshotResponse(BaseModel):
    DBInstance: RDSDBInstanceModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
