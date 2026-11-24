from __future__ import annotations
from pydantic import BaseModel
from .dev_ops_guru_log_anomaly_class import DevOpsGuruLogAnomalyClass


class DevOpsGuruLogAnomalyShowcase(BaseModel):
    LogAnomalyClasses: list[DevOpsGuruLogAnomalyClass] | None = None
