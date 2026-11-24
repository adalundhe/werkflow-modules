from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_sync_function_configuration import AppSyncFunctionConfiguration


class AppSyncListFunctionsResponse(BaseModel):
    functions: list[AppSyncFunctionConfiguration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
