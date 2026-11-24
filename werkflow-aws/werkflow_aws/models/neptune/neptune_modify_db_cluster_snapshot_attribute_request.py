from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NeptuneModifyDBClusterSnapshotAttributeRequest(BaseModel):
    DBClusterSnapshotIdentifier: StrictStr
    AttributeName: StrictStr
    ValuesToAdd: list[StrictStr] | None = None
    ValuesToRemove: list[StrictStr] | None = None
