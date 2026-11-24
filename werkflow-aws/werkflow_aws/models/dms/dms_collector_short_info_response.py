from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSCollectorShortInfoResponse(BaseModel):
    CollectorReferencedId: StrictStr | None = None
    CollectorName: StrictStr | None = None
