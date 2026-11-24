from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_auto_ml_candidate import SageMakerAutoMLCandidate


class SageMakerListCandidatesForAutoMLJobResponse(BaseModel):
    Candidates: list[SageMakerAutoMLCandidate] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
