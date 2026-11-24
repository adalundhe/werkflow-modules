from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DocumentDBDBClusterSnapshotAttribute(BaseModel):
    AttributeName: StrictStr | None = None
    AttributeValues: list[StrictStr] | None = None
