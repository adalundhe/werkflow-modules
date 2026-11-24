from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_code_error import AppSyncCodeError


class AppSyncEvaluateCodeErrorDetail(BaseModel):
    message: StrictStr | None = None
    codeErrors: list[AppSyncCodeError] | None = None
