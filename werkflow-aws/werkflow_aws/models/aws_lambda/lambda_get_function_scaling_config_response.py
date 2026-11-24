from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lambda_function_scaling_config import LambdaFunctionScalingConfig


class LambdaGetFunctionScalingConfigResponse(BaseModel):
    FunctionArn: StrictStr | None = None
    AppliedFunctionScalingConfig: LambdaFunctionScalingConfig | None = None
    RequestedFunctionScalingConfig: LambdaFunctionScalingConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
