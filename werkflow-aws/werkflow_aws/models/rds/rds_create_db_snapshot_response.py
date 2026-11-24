from __future__ import annotations
from pydantic import BaseModel
from .rdsdb_snapshot import RDSDBSnapshot


class RDSCreateDBSnapshotResponse(BaseModel):
    DBSnapshot: RDSDBSnapshot | None = None
