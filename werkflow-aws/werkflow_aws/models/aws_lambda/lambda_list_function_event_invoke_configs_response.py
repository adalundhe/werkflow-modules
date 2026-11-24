from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_function_event_invoke_config import LambdaFunctionEventInvokeConfig


class LambdaListFunctionEventInvokeConfigsResponse(BaseModel):
    FunctionEventInvokeConfigs: list[LambdaFunctionEventInvokeConfig] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
