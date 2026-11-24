from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_runner_service import AppRunnerService


class AppRunnerDescribeServiceResponse(BaseModel):
    Service: AppRunnerService | None = None
    ResponseMetadata: dict[str, Any] | None = None
