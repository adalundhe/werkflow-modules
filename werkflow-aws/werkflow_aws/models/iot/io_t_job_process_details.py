from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTJobProcessDetails(BaseModel):
    processingTargets: list[StrictStr] | None = None
    numberOfCanceledThings: StrictInt | None = None
    numberOfSucceededThings: StrictInt | None = None
    numberOfFailedThings: StrictInt | None = None
    numberOfRejectedThings: StrictInt | None = None
    numberOfQueuedThings: StrictInt | None = None
    numberOfInProgressThings: StrictInt | None = None
    numberOfRemovedThings: StrictInt | None = None
    numberOfTimedOutThings: StrictInt | None = None
