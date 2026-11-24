from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FISExperimentError(BaseModel):
    accountId: StrictStr | None = None
    code: StrictStr | None = None
    location: StrictStr | None = None
