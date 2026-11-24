from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_sync_function_configuration import AppSyncFunctionConfiguration


class AppSyncGetFunctionResponse(BaseModel):
    functionConfiguration: AppSyncFunctionConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
