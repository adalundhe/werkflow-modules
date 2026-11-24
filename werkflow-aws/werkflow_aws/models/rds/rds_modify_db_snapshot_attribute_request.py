from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSModifyDBSnapshotAttributeRequest(BaseModel):
    DBSnapshotIdentifier: StrictStr
    AttributeName: StrictStr
    ValuesToAdd: list[StrictStr] | None = None
    ValuesToRemove: list[StrictStr] | None = None
