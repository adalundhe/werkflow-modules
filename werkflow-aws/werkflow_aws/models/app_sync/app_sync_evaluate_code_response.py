from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_evaluate_code_error_detail import AppSyncEvaluateCodeErrorDetail


class AppSyncEvaluateCodeResponse(BaseModel):
    evaluationResult: StrictStr | None = None
    error: AppSyncEvaluateCodeErrorDetail | None = None
    logs: list[StrictStr] | None = None
    stash: StrictStr | None = None
    outErrors: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
