from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSDBSnapshotAttribute(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeValues: list[StrictStr] | None = None
