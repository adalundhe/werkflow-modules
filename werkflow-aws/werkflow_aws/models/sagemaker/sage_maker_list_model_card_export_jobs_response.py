from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_model_card_export_job_summary import SageMakerModelCardExportJobSummary


class SageMakerListModelCardExportJobsResponse(BaseModel):
    ModelCardExportJobSummaries: list[SageMakerModelCardExportJobSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
