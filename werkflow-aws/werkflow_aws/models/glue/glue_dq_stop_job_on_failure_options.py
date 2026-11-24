from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDQStopJobOnFailureOptions(BaseModel):
    StopJobOnFailureTiming: StrictStr | None = None
