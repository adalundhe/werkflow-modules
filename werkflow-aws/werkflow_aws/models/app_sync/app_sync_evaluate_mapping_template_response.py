from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_error_detail import AppSyncErrorDetail


class AppSyncEvaluateMappingTemplateResponse(BaseModel):
    evaluationResult: StrictStr | None = None
    error: AppSyncErrorDetail | None = None
    logs: list[StrictStr] | None = None
    stash: StrictStr | None = None
    outErrors: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
