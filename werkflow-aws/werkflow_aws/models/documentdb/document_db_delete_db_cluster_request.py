from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DocumentDBDeleteDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    SkipFinalSnapshot: StrictBool | None = None
    FinalDBSnapshotIdentifier: StrictStr | None = None
