from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_trial_component_summary import SageMakerTrialComponentSummary


class SageMakerListTrialComponentsResponse(BaseModel):
    TrialComponentSummaries: list[SageMakerTrialComponentSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
