from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DocumentDBGlobalClusterMember(BaseModel):
    DBClusterArn: StrictStr | None = None
    Readers: list[StrictStr] | None = None
    IsWriter: StrictBool | None = None
    SynchronizationStatus: StrictStr | None = None
