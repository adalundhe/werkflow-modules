from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .compute_optimizer_customizable_metric_parameters import ComputeOptimizerCustomizableMetricParameters


class ComputeOptimizerUtilizationPreference(BaseModel):
    metricName: StrictStr | None = None
    metricParameters: ComputeOptimizerCustomizableMetricParameters | None = None
