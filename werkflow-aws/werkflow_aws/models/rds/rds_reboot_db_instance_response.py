from __future__ import annotations
from pydantic import BaseModel
from .rdsdb_instance import RDSDBInstance


class RDSRebootDBInstanceResponse(BaseModel):
    DBInstance: RDSDBInstance | None = None
