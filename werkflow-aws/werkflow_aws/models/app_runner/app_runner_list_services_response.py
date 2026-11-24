from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_service_summary import AppRunnerServiceSummary


class AppRunnerListServicesResponse(BaseModel):
    ServiceSummaryList: list[AppRunnerServiceSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
