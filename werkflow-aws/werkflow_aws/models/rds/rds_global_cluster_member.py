from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class RDSGlobalClusterMember(BaseModel):
    DBClusterArn: StrictStr | None = None
    Readers: list[StrictStr] | None = None
    IsWriter: StrictBool | None = None
    GlobalWriteForwardingStatus: StrictStr | None = None
    SynchronizationStatus: StrictStr | None = None
