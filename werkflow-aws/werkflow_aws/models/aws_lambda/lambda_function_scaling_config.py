from __future__ import annotations
from pydantic import BaseModel, StrictInt


class LambdaFunctionScalingConfig(BaseModel):
    MinExecutionEnvironments: StrictInt | None = None
    MaxExecutionEnvironments: StrictInt | None = None
