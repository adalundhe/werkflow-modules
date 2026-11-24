from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncSourceApiAssociationConfig(BaseModel):
    mergeType: StrictStr | None = None
