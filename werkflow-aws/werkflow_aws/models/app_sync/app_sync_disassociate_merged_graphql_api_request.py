from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncDisassociateMergedGraphqlApiRequest(BaseModel):
    sourceApiIdentifier: StrictStr
    associationId: StrictStr
