from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSDeleteDBClusterRequest(BaseModel):
    DBClusterIdentifier: StrictStr
    SkipFinalSnapshot: StrictBool | None = None
    FinalDBSnapshotIdentifier: StrictStr | None = None
    DeleteAutomatedBackups: StrictBool | None = None
