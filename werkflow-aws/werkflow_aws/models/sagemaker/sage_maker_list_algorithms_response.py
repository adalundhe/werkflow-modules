from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_algorithm_summary import SageMakerAlgorithmSummary


class SageMakerListAlgorithmsResponse(BaseModel):
    AlgorithmSummaryList: list[SageMakerAlgorithmSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
