from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sage_maker_cleanup_failure import SageMakerCleanupFailure


class SageMakerCleanupStepMetadata(BaseModel):
    CleanedSteps: list[StrictStr] | None = None
    FailedSteps: list[SageMakerCleanupFailure] | None = None
    SkippedSteps: list[StrictStr] | None = None
