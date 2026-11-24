from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDisassociateSourceGraphqlApiRequest(BaseModel):
    mergedApiIdentifier: StrictStr
    associationId: StrictStr
