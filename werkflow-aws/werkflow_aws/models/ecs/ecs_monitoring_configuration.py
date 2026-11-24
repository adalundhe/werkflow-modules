from __future__ import annotations
from pydantic import BaseModel
from .ecs_metric_configuration import ECSMetricConfiguration


class ECSMonitoringConfiguration(BaseModel):
    metricConfigurations: list[ECSMetricConfiguration] | None = None
