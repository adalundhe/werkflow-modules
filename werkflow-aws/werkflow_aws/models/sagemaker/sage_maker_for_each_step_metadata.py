from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .sage_maker_for_each_selector_result import SageMakerForEachSelectorResult


class SageMakerForEachStepMetadata(BaseModel):
    Status: StrictStr | None = None
    InputItemCount: StrictInt | None = None
    TotalStepCount: StrictInt | None = None
    SucceededStepCount: StrictInt | None = None
    FailedStepCount: StrictInt | None = None
    StoppedStepCount: StrictInt | None = None
    Selector: SageMakerForEachSelectorResult | None = None
