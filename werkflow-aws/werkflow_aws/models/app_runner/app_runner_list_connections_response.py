from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_connection_summary import AppRunnerConnectionSummary


class AppRunnerListConnectionsResponse(BaseModel):
    ConnectionSummaryList: list[AppRunnerConnectionSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
