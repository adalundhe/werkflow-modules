from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_runner_service import AppRunnerService


class AppRunnerPauseServiceResponse(BaseModel):
    Service: AppRunnerService | None = None
    OperationId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
