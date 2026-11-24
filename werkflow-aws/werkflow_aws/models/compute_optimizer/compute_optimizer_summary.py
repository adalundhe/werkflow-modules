from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .compute_optimizer_reason_code_summary import ComputeOptimizerReasonCodeSummary


class ComputeOptimizerSummary(BaseModel):
    name: StrictStr | None = None
    value: StrictFloat | StrictInt | None = None
    reasonCodeSummaries: list[ComputeOptimizerReasonCodeSummary] | None = None
