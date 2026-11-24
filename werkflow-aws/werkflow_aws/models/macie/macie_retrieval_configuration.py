from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MacieRetrievalConfiguration(BaseModel):
    externalId: StrictStr | None = None
    retrievalMode: StrictStr | None = None
    roleName: StrictStr | None = None
