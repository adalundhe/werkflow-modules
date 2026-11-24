from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_trial_summary import SageMakerTrialSummary


class SageMakerListTrialsResponse(BaseModel):
    TrialSummaries: list[SageMakerTrialSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
