from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_sync_code_error_location import AppSyncCodeErrorLocation


class AppSyncCodeError(BaseModel):
    errorType: StrictStr | None = None
    value: StrictStr | None = None
    location: AppSyncCodeErrorLocation | None = None
