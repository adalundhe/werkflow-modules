from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .sage_maker_mlflow_app_summary import SageMakerMlflowAppSummary


class SageMakerListMlflowAppsResponse(BaseModel):
    Summaries: list[SageMakerMlflowAppSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
