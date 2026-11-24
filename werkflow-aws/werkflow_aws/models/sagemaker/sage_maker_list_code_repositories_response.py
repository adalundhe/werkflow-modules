from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_code_repository_summary import SageMakerCodeRepositorySummary


class SageMakerListCodeRepositoriesResponse(BaseModel):
    CodeRepositorySummaryList: list[SageMakerCodeRepositorySummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
