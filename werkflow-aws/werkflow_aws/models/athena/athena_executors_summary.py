from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaExecutorsSummary(BaseModel):
    ExecutorId: StrictStr | None = None
    ExecutorType: StrictStr | None = None
    StartDateTime: StrictInt | None = None
    TerminationDateTime: StrictInt | None = None
    ExecutorState: StrictStr | None = None
    ExecutorSize: StrictInt | None = None
