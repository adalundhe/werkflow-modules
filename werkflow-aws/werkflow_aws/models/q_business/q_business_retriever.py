from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessRetriever(BaseModel):
    applicationId: StrictStr | None = None
    retrieverId: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    displayName: StrictStr | None = None
