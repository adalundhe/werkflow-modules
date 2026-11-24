from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailDistributionSubdomain(BaseModel):
    name: StrictStr | None = None
    state: StrictStr | None = None
    errorCode: StrictStr | None = None
    errorDetails: StrictStr | None = None
