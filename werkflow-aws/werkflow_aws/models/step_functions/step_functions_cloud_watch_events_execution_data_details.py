from __future__ import annotations
from pydantic import BaseModel, StrictBool


class StepFunctionsCloudWatchEventsExecutionDataDetails(BaseModel):
    included: StrictBool | None = None
