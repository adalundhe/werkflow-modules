from __future__ import annotations
from pydantic import BaseModel
from .lambda_snap_start_apply_on import LambdaSnapStartApplyOn
from .lambda_snap_start_optimization_status import LambdaSnapStartOptimizationStatus


class LambdaSnapStartResponse(BaseModel):
    ApplyOn: LambdaSnapStartApplyOn | None = None
    OptimizationStatus: LambdaSnapStartOptimizationStatus | None = None
