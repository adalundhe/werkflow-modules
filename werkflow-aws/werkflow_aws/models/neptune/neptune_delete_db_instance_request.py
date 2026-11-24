from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class NeptuneDeleteDBInstanceRequest(BaseModel):
    DBInstanceIdentifier: StrictStr
    SkipFinalSnapshot: StrictBool | None = None
    FinalDBSnapshotIdentifier: StrictStr | None = None
