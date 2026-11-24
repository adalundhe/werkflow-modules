from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneDescribeDBClusterSnapshotAttributesRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
