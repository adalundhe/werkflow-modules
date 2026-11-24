from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_runtime import AppSyncRuntime


class AppSyncEvaluateCodeRequest(BaseModel):
    runtime: AppSyncRuntime
    code: StrictStr
    context: StrictStr
    function: StrictStr | None = None
