from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_operation_summary import AppRunnerOperationSummary


class AppRunnerListOperationsResponse(BaseModel):
    OperationSummaryList: list[AppRunnerOperationSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
