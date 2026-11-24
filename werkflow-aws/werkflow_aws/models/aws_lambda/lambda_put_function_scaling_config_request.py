from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_function_scaling_config import LambdaFunctionScalingConfig


class LambdaPutFunctionScalingConfigRequest(BaseModel):
    FunctionName: StrictStr
    Qualifier: StrictStr
    FunctionScalingConfig: LambdaFunctionScalingConfig | None = None
