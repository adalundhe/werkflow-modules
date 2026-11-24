from __future__ import annotations
from pydantic import BaseModel
from .lambda_snap_start_apply_on import LambdaSnapStartApplyOn


class LambdaSnapStart(BaseModel):
    ApplyOn: LambdaSnapStartApplyOn | None = None
