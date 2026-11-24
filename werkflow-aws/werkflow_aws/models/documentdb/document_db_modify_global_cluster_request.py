from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DocumentDBModifyGlobalClusterRequest(BaseModel):
    GlobalClusterIdentifier: StrictStr
    NewGlobalClusterIdentifier: StrictStr | None = None
    DeletionProtection: StrictBool | None = None
