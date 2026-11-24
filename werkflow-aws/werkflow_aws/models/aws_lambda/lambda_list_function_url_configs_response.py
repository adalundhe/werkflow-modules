from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_function_url_config import LambdaFunctionUrlConfig


class LambdaListFunctionUrlConfigsResponse(BaseModel):
    FunctionUrlConfigs: list[LambdaFunctionUrlConfig] | None = None
    NextMarker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
