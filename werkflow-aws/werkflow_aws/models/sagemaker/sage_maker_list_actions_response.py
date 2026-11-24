from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_action_summary import SageMakerActionSummary


class SageMakerListActionsResponse(BaseModel):
    ActionSummaries: list[SageMakerActionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
