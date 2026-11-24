from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rdsdb_snapshot import RDSDBSnapshot


class RDSDescribeDBSnapshotsResponse(BaseModel):
    Marker: StrictStr | None = None
    DBSnapshots: list[RDSDBSnapshot] | None = None
