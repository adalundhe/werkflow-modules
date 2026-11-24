from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSModifyDBSnapshotRequest(BaseModel):
    DBSnapshotIdentifier: StrictStr
    EngineVersion: StrictStr | None = None
    OptionGroupName: StrictStr | None = None
