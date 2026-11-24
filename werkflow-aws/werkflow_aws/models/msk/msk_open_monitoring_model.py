from __future__ import annotations
from pydantic import BaseModel
from .msk_prometheus_model import MSKPrometheusModel


class MSKOpenMonitoringModel(BaseModel):
    Prometheus: MSKPrometheusModel | None = None
