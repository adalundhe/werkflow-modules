from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncStartSchemaMergeRequest(BaseModel):
    associationId: StrictStr
    mergedApiIdentifier: StrictStr
