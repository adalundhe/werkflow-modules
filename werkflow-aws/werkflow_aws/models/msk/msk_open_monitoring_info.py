from __future__ import annotations
from pydantic import BaseModel
from .msk_prometheus_info import MSKPrometheusInfo


class MSKOpenMonitoringInfo(BaseModel):
    Prometheus: MSKPrometheusInfo | None = None
