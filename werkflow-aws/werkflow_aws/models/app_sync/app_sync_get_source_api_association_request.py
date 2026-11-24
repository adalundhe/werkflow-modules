from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncGetSourceApiAssociationRequest(BaseModel):
    mergedApiIdentifier: StrictStr
    associationId: StrictStr
