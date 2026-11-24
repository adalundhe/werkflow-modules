from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_human_task_ui_summary import SageMakerHumanTaskUiSummary


class SageMakerListHumanTaskUisResponse(BaseModel):
    HumanTaskUiSummaries: list[SageMakerHumanTaskUiSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
