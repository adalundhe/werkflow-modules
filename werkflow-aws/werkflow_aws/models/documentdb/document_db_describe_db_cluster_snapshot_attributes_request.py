from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDescribeDBClusterSnapshotAttributesRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
