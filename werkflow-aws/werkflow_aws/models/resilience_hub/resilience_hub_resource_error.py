from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ResilienceHubResourceError(BaseModel):
    logicalResourceId: StrictStr | None = None
    physicalResourceId: StrictStr | None = None
    reason: StrictStr | None = None
