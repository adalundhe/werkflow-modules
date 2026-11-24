from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDescribeDBSnapshotAttributesRequest(BaseModel):
    DBSnapshotIdentifier: StrictStr
